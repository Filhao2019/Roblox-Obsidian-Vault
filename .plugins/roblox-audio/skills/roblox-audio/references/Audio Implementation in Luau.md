---
title: Audio Implementation in Luau
date: 2026-11-02
tags: [audio, luau, code, soundmanager, audioplayer]
status: untested
---

# Audio Implementation in Luau

Original, typed Luau for a game audio layer: a pooled `SoundManager` with pitch/volume jitter, 2D and 3D playback, SoundGroup volume settings, music ducking, a footstep system keyed on `Humanoid.FloorMaterial`, combo pitch escalation, and an example using the newer Audio API (AudioPlayer, AudioEmitter, AudioListener, AudioDeviceOutput, Wire, effects). **Everything here is `status: untested`**: paste into Studio, replace the placeholder asset IDs (`rbxassetid://0`) with your own uploads or Creator Store audio you may use, and playtest. Design rationale: [[What Makes a Sound Satisfying]], [[Combat and Impact Sounds]], [[UI Sounds]], [[Ambience and Music]]. Wider architecture: [[Project Architecture and Frameworks]]; remotes for replicating positional sounds: [[Networking and Remotes]].

## Layout

```
ReplicatedStorage/
  Audio/
    SoundManager   (ModuleScript, client)
    SoundCatalog   (ModuleScript, data)
    ComboPitch     (ModuleScript)
    Footsteps      (ModuleScript, client)
    AudioApiDemo   (ModuleScript, client or server)
StarterPlayerScripts/AudioBootstrap (LocalScript)
```

## SoundCatalog (data)

```luau
--!strict
-- ReplicatedStorage/Audio/SoundCatalog
export type SoundDef = {
	id: string,
	group: string, -- "Music" | "SFX" | "UI" | "Ambience"
	volume: number?,
	pitchMin: number?,
	pitchMax: number?,
	volumeJitter: number?, -- +/- fraction, e.g. 0.08
	maxVoices: number?,
	rolloffMin: number?,
	rolloffMax: number?,
}

local PLACEHOLDER = "rbxassetid://0" -- replace with real, permitted assets

local Catalog: { [string]: SoundDef } = {
	UiClick = { id = PLACEHOLDER, group = "UI", volume = 0.5, pitchMin = 0.96, pitchMax = 1.04, maxVoices = 4 },
	UiError = { id = PLACEHOLDER, group = "UI", volume = 0.6, maxVoices = 2 },
	Coin = { id = PLACEHOLDER, group = "SFX", volume = 0.6, pitchMin = 1, pitchMax = 1, maxVoices = 8 },
	Hit = { id = PLACEHOLDER, group = "SFX", volume = 0.8, pitchMin = 0.93, pitchMax = 1.07, volumeJitter = 0.1, maxVoices = 6, rolloffMin = 10, rolloffMax = 120 },
	Stinger = { id = PLACEHOLDER, group = "SFX", volume = 0.9, maxVoices = 2 },
	-- Footstep sets: one definition per bucket (see Footsteps module)
	Step_Stone = { id = PLACEHOLDER, group = "SFX", volume = 0.35, pitchMin = 0.9, pitchMax = 1.1, volumeJitter = 0.12, maxVoices = 6, rolloffMin = 6, rolloffMax = 60 },
	Step_Wood = { id = PLACEHOLDER, group = "SFX", volume = 0.35, pitchMin = 0.9, pitchMax = 1.1, volumeJitter = 0.12, maxVoices = 6, rolloffMin = 6, rolloffMax = 60 },
	Step_Metal = { id = PLACEHOLDER, group = "SFX", volume = 0.35, pitchMin = 0.9, pitchMax = 1.1, volumeJitter = 0.12, maxVoices = 6, rolloffMin = 6, rolloffMax = 60 },
	Step_Grass = { id = PLACEHOLDER, group = "SFX", volume = 0.3, pitchMin = 0.9, pitchMax = 1.1, volumeJitter = 0.12, maxVoices = 6, rolloffMin = 6, rolloffMax = 60 },
	Step_Sand = { id = PLACEHOLDER, group = "SFX", volume = 0.3, pitchMin = 0.9, pitchMax = 1.1, volumeJitter = 0.12, maxVoices = 6, rolloffMin = 6, rolloffMax = 60 },
	Step_Default = { id = PLACEHOLDER, group = "SFX", volume = 0.3, pitchMin = 0.9, pitchMax = 1.1, volumeJitter = 0.12, maxVoices = 6, rolloffMin = 6, rolloffMax = 60 },
}

return Catalog
```

A single asset can hold several variants; for a real game register `Step_Stone_1..4` and have the manager choose randomly (see `variants` extension below).

## SoundManager

```luau
--!strict
-- ReplicatedStorage/Audio/SoundManager  (use from the client)
local SoundService = game:GetService("SoundService")
local TweenService = game:GetService("TweenService")
local Workspace = game:GetService("Workspace")

local Catalog = require(script.Parent.SoundCatalog)
type SoundDef = Catalog.SoundDef

type Voice = {
	sound: Sound,
	busy: boolean,
	startedAt: number,
}

type Pool = {
	def: SoundDef,
	voices: { Voice },
}

local SoundManager = {}

local GROUP_NAMES = { "Music", "SFX", "UI", "Ambience" }
local groups: { [string]: SoundGroup } = {}
local userVolume: { [string]: number } = {} -- player settings, 0..1
local baseVolume: { [string]: number } = {} -- group base, ducking is applied on top
local pools: { [string]: Pool } = {}
local duckTokens: { [string]: number } = {}
local rng = Random.new()

local masterGroup: SoundGroup

local function makeGroup(name: string, parent: Instance): SoundGroup
	local g = Instance.new("SoundGroup")
	g.Name = name
	g.Volume = 1
	g.Parent = parent
	return g
end

function SoundManager.init()
	if masterGroup then
		return
	end
	masterGroup = makeGroup("Master", SoundService)
	for _, name in GROUP_NAMES do
		groups[name] = makeGroup(name, masterGroup)
		userVolume[name] = 1
		baseVolume[name] = 1
	end
end

-- Settings ----------------------------------------------------------------

function SoundManager.setUserVolume(groupName: string, value: number)
	local g = groups[groupName]
	if not g then
		return
	end
	userVolume[groupName] = math.clamp(value, 0, 1)
	g.Volume = baseVolume[groupName] * userVolume[groupName]
end

function SoundManager.getUserVolume(groupName: string): number
	return userVolume[groupName] or 1
end

function SoundManager.setMasterVolume(value: number)
	masterGroup.Volume = math.clamp(value, 0, 1)
end

-- Pooling -----------------------------------------------------------------

local function newVoice(def: SoundDef): Voice
	local s = Instance.new("Sound")
	s.SoundId = def.id
	s.SoundGroup = groups[def.group]
	s.RollOffMinDistance = def.rolloffMin or 10
	s.RollOffMaxDistance = def.rolloffMax or 100
	s.Parent = SoundService -- idle parking spot (2D behaviour)
	return { sound = s, busy = false, startedAt = 0 }
end

local function getPool(name: string): Pool?
	local pool = pools[name]
	if pool then
		return pool
	end
	local def = Catalog[name]
	if not def then
		warn("SoundManager: unknown sound", name)
		return nil
	end
	pool = { def = def, voices = {} }
	pools[name] = pool
	return pool
end

local function acquire(pool: Pool): Voice?
	for _, v in pool.voices do
		if not v.busy then
			return v
		end
	end
	local limit = pool.def.maxVoices or 8
	if #pool.voices < limit then
		local v = newVoice(pool.def)
		table.insert(pool.voices, v)
		return v
	end
	-- Voice stealing: take the oldest instance so new events are never silent.
	local oldest: Voice? = nil
	for _, v in pool.voices do
		if oldest == nil or v.startedAt < oldest.startedAt then
			oldest = v
		end
	end
	if oldest then
		oldest.sound:Stop()
	end
	return oldest
end

local function release(v: Voice)
	v.busy = false
	v.sound.Parent = SoundService
end

local function configure(v: Voice, def: SoundDef, pitchMul: number?)
	local pitch = rng:NextNumber(def.pitchMin or 1, def.pitchMax or 1) * (pitchMul or 1)
	local jitter = def.volumeJitter or 0
	local vol = (def.volume or 1) * (1 + rng:NextNumber(-jitter, jitter))
	v.sound.PlaybackSpeed = pitch
	v.sound.Volume = math.max(vol, 0)
	v.sound.TimePosition = 0
end

local function start(v: Voice)
	v.busy = true
	v.startedAt = os.clock()
	local done = false
	local function finish()
		if done then
			return
		end
		done = true
		release(v)
	end
	v.sound.Ended:Once(finish)
	v.sound.Stopped:Once(finish)
	v.sound:Play()
end

-- Public playback ---------------------------------------------------------

-- 2D: UI, music stingers, local feedback. pitchMul multiplies the random pitch.
function SoundManager.play2D(name: string, pitchMul: number?): Sound?
	local pool = getPool(name)
	if not pool then
		return nil
	end
	local v = acquire(pool)
	if not v then
		return nil
	end
	v.sound.Parent = SoundService
	configure(v, pool.def, pitchMul)
	start(v)
	return v.sound
end

-- 3D: parent the sound to a BasePart/Attachment, or give a world position.
local anchorPart: Part? = nil
local function getAnchor(): Part
	if anchorPart and anchorPart.Parent then
		return anchorPart
	end
	local p = Instance.new("Part")
	p.Name = "AudioAnchor"
	p.Anchored = true
	p.CanCollide = false
	p.CanQuery = false
	p.CanTouch = false
	p.Transparency = 1
	p.Size = Vector3.new(0.1, 0.1, 0.1)
	p.Parent = Workspace
	anchorPart = p
	return p
end

function SoundManager.play3D(name: string, target: Instance | Vector3, pitchMul: number?): Sound?
	local pool = getPool(name)
	if not pool then
		return nil
	end
	local v = acquire(pool)
	if not v then
		return nil
	end
	configure(v, pool.def, pitchMul)
	if typeof(target) == "Vector3" then
		-- One attachment per call, parented to a shared invisible anchor part.
		local att = Instance.new("Attachment")
		att.WorldPosition = target
		att.Parent = getAnchor()
		v.sound.Parent = att
		v.sound.Ended:Once(function()
			att:Destroy()
		end)
		v.sound.Stopped:Once(function()
			att:Destroy()
		end)
	else
		v.sound.Parent = target
	end
	start(v)
	return v.sound
end

-- Ducking -----------------------------------------------------------------

-- Lowers a group's multiplier, holds, then restores. Overlapping calls are
-- handled with a token so only the latest call restores the volume.
function SoundManager.duck(groupName: string, depth: number, hold: number, fadeIn: number?, fadeOut: number?)
	local g = groups[groupName]
	if not g then
		return
	end
	local token = (duckTokens[groupName] or 0) + 1
	duckTokens[groupName] = token
	local full = baseVolume[groupName] * userVolume[groupName]
	local ducked = full * math.clamp(depth, 0, 1)
	TweenService:Create(g, TweenInfo.new(fadeIn or 0.08, Enum.EasingStyle.Quad, Enum.EasingDirection.Out), { Volume = ducked }):Play()
	task.delay(hold, function()
		if duckTokens[groupName] ~= token then
			return
		end
		local restore = baseVolume[groupName] * userVolume[groupName]
		TweenService:Create(g, TweenInfo.new(fadeOut or 0.6, Enum.EasingStyle.Sine, Enum.EasingDirection.In), { Volume = restore }):Play()
	end)
end

-- Plays a stinger and ducks music and ambience while it plays.
function SoundManager.playStinger(name: string)
	local s = SoundManager.play2D(name)
	if not s then
		return
	end
	local length = if s.IsLoaded then s.TimeLength else 2
	SoundManager.duck("Music", 0.35, math.max(length - 0.3, 0.2))
	SoundManager.duck("Ambience", 0.5, math.max(length - 0.3, 0.2))
end

-- Preload ---------------------------------------------------------------

function SoundManager.preload(names: { string })
	local assets: { Instance } = {}
	for _, n in names do
		local pool = getPool(n)
		if pool then
			local v = newVoice(pool.def)
			table.insert(pool.voices, v)
			table.insert(assets, v.sound)
		end
	end
	game:GetService("ContentProvider"):PreloadAsync(assets)
end

return SoundManager
```

Notes:
- `Sound.Ended` and `Stopped` events exist on the legacy Sound class ([Sound](https://create.roblox.com/docs/reference/engine/classes/Sound)); `SoundGroup.Volume` scales children and groups can nest ([sound groups](https://create.roblox.com/docs/sound/groups)).
- Legacy Sounds parented to a part or attachment are positional, to SoundService/Workspace they are not ([Sound objects](https://create.roblox.com/docs/sound/objects)).
- Roblox now steers new work to the audio objects (below); the legacy path is simplest for UI and quick effects. A group-level compressor with a side chain is the engine-side way to duck ([sound groups](https://create.roblox.com/docs/sound/groups)).

## ComboPitch (rewarding escalation)

```luau
--!strict
-- ReplicatedStorage/Audio/ComboPitch
local ComboPitch = {}
ComboPitch.__index = ComboPitch

export type Combo = typeof(setmetatable(
	{} :: {
		step: number,
		maxSteps: number,
		resetAfter: number,
		count: number,
		lastTime: number,
	},
	ComboPitch
))

-- stepSemitones: pitch rise per hit; maxSteps: cap; resetAfter: seconds without a hit
function ComboPitch.new(stepSemitones: number?, maxSteps: number?, resetAfter: number?): Combo
	return setmetatable({
		step = stepSemitones or 1,
		maxSteps = maxSteps or 12,
		resetAfter = resetAfter or 1.2,
		count = 0,
		lastTime = -math.huge,
	}, ComboPitch)
end

-- Returns a playback-speed multiplier for this hit and advances the combo.
function ComboPitch.next(self: Combo): number
	local now = os.clock()
	if now - self.lastTime > self.resetAfter then
		self.count = 0
	end
	self.lastTime = now
	local multiplier = 2 ^ ((self.count * self.step) / 12)
	self.count = math.min(self.count + 1, self.maxSteps)
	return multiplier
end

function ComboPitch.reset(self: Combo)
	self.count = 0
end

return ComboPitch
```

Usage with the manager (coin streak):

```luau
local SoundManager = require(game.ReplicatedStorage.Audio.SoundManager)
local ComboPitch = require(game.ReplicatedStorage.Audio.ComboPitch)
SoundManager.init()
local coinCombo = ComboPitch.new(1, 12, 1.0)
local function onCoinCollected()
	SoundManager.play2D("Coin", coinCombo:next())
end
```

Pitch via `PlaybackSpeed` also changes duration; at +12 semitones the sound is half as long, which is usually fine for blips. If it is not, use the new-API pitch shifter ([AudioPitchShifter](https://create.roblox.com/docs/reference/engine/classes/AudioPitchShifter)).

## Footsteps by FloorMaterial

```luau
--!strict
-- ReplicatedStorage/Audio/Footsteps  (client, one controller per character)
local RunService = game:GetService("RunService")
local SoundManager = require(script.Parent.SoundManager)

local BUCKET_BY_MATERIAL: { [Enum.Material]: string } = {
	[Enum.Material.Concrete] = "Stone",
	[Enum.Material.Pavement] = "Stone",
	[Enum.Material.Asphalt] = "Stone",
	[Enum.Material.Brick] = "Stone",
	[Enum.Material.Cobblestone] = "Stone",
	[Enum.Material.Rock] = "Stone",
	[Enum.Material.Slate] = "Stone",
	[Enum.Material.Granite] = "Stone",
	[Enum.Material.Marble] = "Stone",
	[Enum.Material.CeramicTiles] = "Stone",
	[Enum.Material.Wood] = "Wood",
	[Enum.Material.WoodPlanks] = "Wood",
	[Enum.Material.Metal] = "Metal",
	[Enum.Material.DiamondPlate] = "Metal",
	[Enum.Material.CorrodedMetal] = "Metal",
	[Enum.Material.Grass] = "Grass",
	[Enum.Material.LeafyGrass] = "Grass",
	[Enum.Material.Ground] = "Grass",
	[Enum.Material.Mud] = "Grass",
	[Enum.Material.Sand] = "Sand",
	[Enum.Material.Sandstone] = "Sand",
	[Enum.Material.Snow] = "Sand",
}

local STRIDE = 7.5 -- studs between footsteps while walking; tune per game

export type Controller = {
	destroy: (self: Controller) -> (),
	setEnabled: (self: Controller, enabled: boolean) -> (),
}

local Footsteps = {}

function Footsteps.attach(character: Model): Controller
	local humanoid = character:WaitForChild("Humanoid") :: Humanoid
	local root = character:WaitForChild("HumanoidRootPart") :: BasePart
	local enabled = true
	local distance = 0
	local lastPos = root.Position

	local conn = RunService.Heartbeat:Connect(function()
		if not enabled then
			return
		end
		local material = humanoid.FloorMaterial
		if material == Enum.Material.Air or humanoid.MoveDirection.Magnitude < 0.1 then
			lastPos = root.Position
			return
		end
		local pos = root.Position
		local flat = Vector3.new(pos.X - lastPos.X, 0, pos.Z - lastPos.Z).Magnitude
		lastPos = pos
		distance += flat
		if distance >= STRIDE then
			distance -= STRIDE
			local bucket = BUCKET_BY_MATERIAL[material] or "Default"
			local name = "Step_" .. bucket
			-- Crouch/sprint scaling can be added by passing a pitch multiplier.
			SoundManager.play3D(name, root)
		end
	end)

	local controller = {} :: Controller
	function controller.destroy(_self: Controller)
		conn:Disconnect()
	end
	function controller.setEnabled(_self: Controller, value: boolean)
		enabled = value
	end
	return controller
end

return Footsteps
```

Notes: `Humanoid.FloorMaterial` is read-only and not replicated ([Humanoid](https://create.roblox.com/docs/reference/engine/classes/Humanoid)), so run this on each client for *other* characters as well (it will read the local simulation of their humanoid) or replicate step events from the server. The `Enum.Material` list is in the [Material enum](https://create.roblox.com/docs/reference/engine/enums/Material). Add landing sounds by listening to `humanoid.StateChanged` for `Landed`.

## Bootstrap (client)

```luau
--!strict
-- StarterPlayerScripts/AudioBootstrap
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Audio = ReplicatedStorage:WaitForChild("Audio")
local SoundManager = require(Audio:WaitForChild("SoundManager"))
local Footsteps = require(Audio:WaitForChild("Footsteps"))

SoundManager.init()
SoundManager.preload({ "UiClick", "Coin", "Hit" })

local player = Players.LocalPlayer
local function onCharacter(character: Model)
	Footsteps.attach(character)
end
if player.Character then
	onCharacter(player.Character)
end
player.CharacterAdded:Connect(onCharacter)

-- Example settings hook (connect to your settings UI sliders)
-- SoundManager.setUserVolume("Music", 0.6)
```

## New Audio API: players, emitters, listeners, wires, effects

Concepts from the docs ([audio objects](https://create.roblox.com/docs/audio/objects)): `AudioPlayer` plays an asset, `AudioEmitter` is a virtual speaker in 3D space, `AudioListener` is a virtual microphone, `AudioDeviceOutput` is the player's speakers, and a `Wire` carries a stream from `SourceInstance` to `TargetInstance`. Effects sit in the chain between player and output ([audio effects](https://create.roblox.com/docs/audio/effects)). 2D audio is player -> output; 3D is player -> emitter, plus listener -> output; set `SoundService.DefaultListenerLocation` to Character so each player has a listener ([3D tutorial](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-3D-audio), [SoundService](https://create.roblox.com/docs/reference/engine/classes/SoundService)). Distance volume is `AudioEmitter` `DistanceAttenuation`, a studs-to-volume curve you set with `SetDistanceAttenuation` ([AudioEmitter](https://create.roblox.com/docs/reference/engine/classes/AudioEmitter)).

```luau
--!strict
-- ReplicatedStorage/Audio/AudioApiDemo
local SoundService = game:GetService("SoundService")

local AudioApiDemo = {}

local function wire(source: Instance, target: Instance, targetName: string?): Wire
	local w = Instance.new("Wire")
	w.SourceInstance = source
	w.TargetInstance = target
	if targetName then
		w.TargetName = targetName -- pin name, e.g. "Sidechain"
	end
	w.Parent = target
	return w
end

-- Run once (server or client) so every player has a listener on their character.
function AudioApiDemo.setupListener()
	SoundService.DefaultListenerLocation = Enum.ListenerLocation.Character
end

-- 2D sound: AudioPlayer -> AudioDeviceOutput (everyone hears it equally).
function AudioApiDemo.create2D(assetId: string, looping: boolean, volume: number): AudioPlayer
	local player = Instance.new("AudioPlayer")
	player.Asset = assetId
	player.Looping = looping
	player.Volume = volume
	player.Parent = SoundService

	local output = Instance.new("AudioDeviceOutput")
	output.Parent = SoundService

	wire(player, output)
	return player
end

-- 3D sound on a part: AudioPlayer -> AudioEmitter, with a falloff curve (studs -> volume).
function AudioApiDemo.create3D(part: BasePart, assetId: string, looping: boolean): AudioPlayer
	local player = Instance.new("AudioPlayer")
	player.Asset = assetId
	player.Looping = looping
	player.Parent = part

	local emitter = Instance.new("AudioEmitter")
	emitter:SetDistanceAttenuation({
		[0] = 1,
		[20] = 0.8,
		[40] = 0.4,
		[80] = 0,
	})
	emitter.Parent = part

	wire(player, emitter)
	return player
end

-- Muffle everything when underwater: player -> equalizer -> output.
function AudioApiDemo.createMuffledLoop(assetId: string): (AudioPlayer, AudioEqualizer)
	local player = Instance.new("AudioPlayer")
	player.Asset = assetId
	player.Looping = true
	player.Parent = SoundService

	local eq = Instance.new("AudioEqualizer")
	eq.HighGain = -30
	eq.MidGain = -6
	eq.Parent = SoundService

	local output = Instance.new("AudioDeviceOutput")
	output.Parent = SoundService

	wire(player, eq)
	wire(eq, output)
	return player, eq
end

-- Sidechain ducking: music -> compressor -> output, trigger -> compressor "Sidechain" pin.
-- Threshold/Ratio/Attack/Release values are starting points; check units in the
-- AudioCompressor reference and tune by ear.
function AudioApiDemo.createDuckedMusic(musicAsset: string, triggerAsset: string): (AudioPlayer, AudioPlayer)
	local music = Instance.new("AudioPlayer")
	music.Asset = musicAsset
	music.Looping = true
	music.Parent = SoundService

	local trigger = Instance.new("AudioPlayer")
	trigger.Asset = triggerAsset
	trigger.Parent = SoundService

	local compressor = Instance.new("AudioCompressor")
	compressor.Threshold = -30
	compressor.Ratio = 8
	compressor.Attack = 0.02
	compressor.Release = 0.5
	compressor.Parent = SoundService

	local output = Instance.new("AudioDeviceOutput")
	output.Parent = SoundService

	wire(music, compressor) -- main input
	wire(trigger, compressor, "Sidechain") -- drives the gain reduction
	wire(compressor, output)
	wire(trigger, output) -- the trigger itself must still be audible

	return music, trigger
end

-- Fade a player with an AudioFader: player -> fader -> output.
function AudioApiDemo.createFader(player: AudioPlayer): AudioFader
	local fader = Instance.new("AudioFader")
	fader.Volume = 1
	fader.Parent = SoundService
	local output = Instance.new("AudioDeviceOutput")
	output.Parent = SoundService
	wire(player, fader)
	wire(fader, output)
	return fader
end

return AudioApiDemo
```

Usage:

```luau
local Demo = require(game.ReplicatedStorage.Audio.AudioApiDemo)
Demo.setupListener()
local music, trigger = Demo.createDuckedMusic("rbxassetid://0", "rbxassetid://0")
music:Play()
-- later, on a rare drop:
trigger:Play()
```

Caveats (all untested): the `AudioPlayer.Asset` property takes a content URL while `AssetId` is deprecated ([AudioPlayer](https://create.roblox.com/docs/reference/engine/classes/AudioPlayer)); wire direction and pin names should be verified in Studio; effect parameter ranges are not documented on the class pages. A player is `IsReady` only after loading, so wait or preload before `Play()`. `SoundService.DefaultListenerLocation` is the documented name on the SoundService page.

## Testing checklist

1. Replace placeholders; confirm each asset loads (Output shows 403 for private audio, see [[Sound Sources and Libraries]]).
2. Spam a pooled sound faster than `maxVoices`; no errors and no runaway instance count.
3. Check ducking restores volume after overlapping stingers.
4. Walk over each material and confirm the bucket.
5. Test on mobile for CPU and memory; keep simultaneous sounds modest ([[Performance Budgets and Optimization]], [[Code Performance and Optimization]]).

## References

- [Roblox: audio objects](https://create.roblox.com/docs/audio/objects) — docs · players, emitters, wires
- [Roblox: audio effects](https://create.roblox.com/docs/audio/effects) — docs · effect chain
- [Roblox: audio overview](https://create.roblox.com/docs/audio) — docs · instance list
- [Roblox: add 2D audio](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-2D-audio) — tutorial · 2D setup (link seen on audio page)
- [Roblox: add 3D audio](https://create.roblox.com/docs/tutorials/use-case-tutorials/audio/add-3D-audio) — tutorial · attenuation curve
- [Roblox: AudioPlayer](https://create.roblox.com/docs/reference/engine/classes/AudioPlayer) — docs · properties and methods
- [Roblox: AudioEmitter](https://create.roblox.com/docs/reference/engine/classes/AudioEmitter) — docs · SetDistanceAttenuation
- [Roblox: AudioListener](https://create.roblox.com/docs/reference/engine/classes/AudioListener) — docs · listener
- [Roblox: AudioDeviceOutput](https://create.roblox.com/docs/reference/engine/classes/AudioDeviceOutput) — docs · output device
- [Roblox: Wire](https://create.roblox.com/docs/reference/engine/classes/Wire) — docs · source/target
- [Roblox: AudioCompressor](https://create.roblox.com/docs/reference/engine/classes/AudioCompressor) — docs · Sidechain pin
- [Roblox: AudioFader](https://create.roblox.com/docs/reference/engine/classes/AudioFader) — docs · volume stage
- [Roblox: AudioEqualizer](https://create.roblox.com/docs/reference/engine/classes/AudioEqualizer) — docs · band gains
- [Roblox: AudioPitchShifter](https://create.roblox.com/docs/reference/engine/classes/AudioPitchShifter) — docs · pitch without speed
- [Roblox: AudioLimiter](https://create.roblox.com/docs/reference/engine/classes/AudioLimiter) — docs · master limiter
- [Roblox: AudioReverb](https://create.roblox.com/docs/reference/engine/classes/AudioReverb) — docs · reverb
- [Roblox: Sound](https://create.roblox.com/docs/reference/engine/classes/Sound) — docs · legacy sound
- [Roblox: SoundGroup](https://create.roblox.com/docs/reference/engine/classes/SoundGroup) — docs · groups
- [Roblox: sound groups guide](https://create.roblox.com/docs/sound/groups) — docs · nesting, ducking
- [Roblox: Sound objects guide](https://create.roblox.com/docs/sound/objects) — docs · positional by parent
- [Roblox: dynamic effects](https://create.roblox.com/docs/sound/dynamic-effects) — docs · legacy effects
- [Roblox: SoundService](https://create.roblox.com/docs/reference/engine/classes/SoundService) — docs · listener location, PlayLocalSound
- [Roblox: Humanoid](https://create.roblox.com/docs/reference/engine/classes/Humanoid) — docs · FloorMaterial
- [Roblox: Material enum](https://create.roblox.com/docs/reference/engine/enums/Material) — docs · material list
- [Roblox docs index (llms.txt)](https://create.roblox.com/docs/llms.txt) — docs · full audio class list
- [Wikipedia: dynamic range compression](https://en.wikipedia.org/wiki/Dynamic_range_compression) — encyclopedia · sidechain concept


## Visual study

- [[Spatial Audio Visual Study]] — embedded reference images and short clips, with study prompts and attribution.


Links: [[Audio MOC]] · [[00 Home]]
