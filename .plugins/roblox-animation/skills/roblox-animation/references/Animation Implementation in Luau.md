---
title: Animation Implementation in Luau
date: 2026-11-02
tags: [animation, luau, code, cutscenes, camera]
status: untested
---

# Animation Implementation in Luau

Original reference modules for animation playback, markers, procedural motion, a camera cutscene player and camera shake. All code is untested; test in Studio before shipping. Put client modules in `ReplicatedStorage` or `StarterPlayerScripts`. Animation asset IDs shown as `rbxassetid://0` are placeholders.

## 1. AnimationPlayer (load, cache, play)

```lua
--!strict
-- ModuleScript: AnimationPlayer
local AnimationPlayer = {}
AnimationPlayer.__index = AnimationPlayer

export type PlayOptions = {
	fade: number?,
	weight: number?,
	speed: number?,
	priority: Enum.AnimationPriority?,
	looped: boolean?,
}

export type Player = typeof(setmetatable({} :: {
	_animator: Animator,
	_tracks: { [string]: AnimationTrack },
	_anims: { [string]: Animation },
}, AnimationPlayer))

function AnimationPlayer.new(rig: Model): Player
	-- Humanoid rigs have an Animator under Humanoid; others under AnimationController.
	local host = rig:FindFirstChildOfClass("Humanoid") or rig:FindFirstChildOfClass("AnimationController")
	assert(host, "Rig needs a Humanoid or AnimationController")
	local animator = host:FindFirstChildOfClass("Animator")
	if not animator then
		animator = Instance.new("Animator")
		animator.Parent = host
	end
	return setmetatable({
		_animator = animator :: Animator,
		_tracks = {},
		_anims = {},
	}, AnimationPlayer)
end

function AnimationPlayer.register(self: Player, name: string, assetId: string)
	local anim = Instance.new("Animation")
	anim.AnimationId = assetId
	self._anims[name] = anim
	self._tracks[name] = self._animator:LoadAnimation(anim)
end

function AnimationPlayer.play(self: Player, name: string, opts: PlayOptions?): AnimationTrack?
	local track = self._tracks[name]
	if not track then
		warn("Unknown animation: " .. name)
		return nil
	end
	local o: PlayOptions = opts or {}
	if o.priority then
		track.Priority = o.priority
	end
	if o.looped ~= nil then
		track.Looped = o.looped
	end
	track:Play(o.fade or 0.1, o.weight or 1, o.speed or 1)
	return track
end

function AnimationPlayer.stop(self: Player, name: string, fade: number?)
	local track = self._tracks[name]
	if track then
		track:Stop(fade or 0.1)
	end
end

function AnimationPlayer.destroy(self: Player)
	for _, track in self._tracks do
		track:Stop(0)
		track:Destroy()
	end
	for _, anim in self._anims do
		anim:Destroy()
	end
	table.clear(self._tracks)
	table.clear(self._anims)
end

return AnimationPlayer
```

Usage: create one per character on `CharacterAdded`, register clips once, destroy on removal. Loading each clip once per rig avoids repeated `LoadAnimation` calls.

## 2. Keyframe marker events

```lua
--!strict
-- Connect markers authored in the Animation Editor (e.g. "Footstep", "HitStart", "HitEnd").
local function bindMarkers(track: AnimationTrack, handlers: { [string]: (param: string) -> () }): { RBXScriptConnection }
	local conns = {}
	for markerName, handler in handlers do
		table.insert(conns, track:GetMarkerReachedSignal(markerName):Connect(handler))
	end
	return conns
end

-- Example
-- local conns = bindMarkers(runTrack, {
-- 	Footstep = function(param) playFootstepSound(param) end, -- param e.g. "L" or "R"
-- })
```

Connect before `Play` so the first marker is not missed. For combat, send hit markers to the server only as a request; the server validates timing and range ([[Combat Systems]]).

## 3. Procedural lean and tilt while running

```lua
--!strict
-- Applies a Motor6D C0 offset to the root joint based on velocity. R15: LowerTorso.Root.
local RunService = game:GetService("RunService")

local function startLean(character: Model, maxLeanDeg: number, smoothing: number): () -> ()
	local humanoid = character:WaitForChild("Humanoid") :: Humanoid
	local root = character:WaitForChild("HumanoidRootPart") :: BasePart
	local lowerTorso = character:WaitForChild("LowerTorso") :: BasePart
	local joint = lowerTorso:WaitForChild("Root") :: Motor6D
	local baseC0 = joint.C0
	local lean = Vector2.zero -- x: pitch (forward), y: roll (sideways)

	local conn = RunService.RenderStepped:Connect(function(dt: number)
		local vel = root.AssemblyLinearVelocity
		local localVel = root.CFrame:VectorToObjectSpace(Vector3.new(vel.X, 0, vel.Z))
		local speedRatio = math.clamp(localVel.Magnitude / math.max(humanoid.WalkSpeed, 1), 0, 1.5)
		local forward = math.clamp(-localVel.Z / math.max(humanoid.WalkSpeed, 1), -1, 1)
		local side = math.clamp(localVel.X / math.max(humanoid.WalkSpeed, 1), -1, 1)
		local target = Vector2.new(forward * speedRatio, -side * speedRatio) * math.rad(maxLeanDeg)
		local alpha = 1 - math.exp(-smoothing * dt) -- frame-rate independent smoothing
		lean = lean:Lerp(target, alpha)
		joint.C0 = baseC0 * CFrame.Angles(lean.X, 0, lean.Y)
	end)

	return function()
		conn:Disconnect()
		joint.C0 = baseC0
	end
end

return startLean
```

Note: setting Motor6D C0 on the client is local only; other players do not see it unless you replicate. Animation tracks that drive the same joint may overwrite C0 changes depending on playback order; test with your clips (unverified).

## 4. Head look-at

```lua
--!strict
-- Rotates the Neck toward a target point, clamped. R15: Head.Neck.
local RunService = game:GetService("RunService")

local function startHeadLook(character: Model, getTarget: () -> Vector3?, maxYawDeg: number, maxPitchDeg: number): () -> ()
	local head = character:WaitForChild("Head") :: BasePart
	local neck = head:WaitForChild("Neck") :: Motor6D
	local baseC0 = neck.C0
	local yaw, pitch = 0, 0

	local conn = RunService.RenderStepped:Connect(function(dt: number)
		local target = getTarget()
		local targetYaw, targetPitch = 0, 0
		if target then
			local torso = (character:FindFirstChild("UpperTorso") or character:FindFirstChild("Torso")) :: BasePart?
			if torso then
				local rel = torso.CFrame:PointToObjectSpace(target)
				targetYaw = math.clamp(math.atan2(-rel.X, -rel.Z), -math.rad(maxYawDeg), math.rad(maxYawDeg))
				targetPitch = math.clamp(math.atan2(rel.Y, math.sqrt(rel.X ^ 2 + rel.Z ^ 2)), -math.rad(maxPitchDeg), math.rad(maxPitchDeg))
			end
		end
		local alpha = 1 - math.exp(-8 * dt)
		yaw += (targetYaw - yaw) * alpha
		pitch += (targetPitch - pitch) * alpha
		neck.C0 = baseC0 * CFrame.Angles(pitch, yaw, 0)
	end)

	return function()
		conn:Disconnect()
		neck.C0 = baseC0
	end
end

return startHeadLook
```

## 5. Sprint FOV change

```lua
--!strict
local TweenService = game:GetService("TweenService")

local function setSprintFov(camera: Camera, sprinting: boolean, baseFov: number, sprintFov: number)
	local goal = sprinting and sprintFov or baseFov
	TweenService:Create(camera, TweenInfo.new(0.25, Enum.EasingStyle.Quad, Enum.EasingDirection.Out), { FieldOfView = goal }):Play()
end

return setSprintFov
```

## 6. CutscenePlayer

Camera keyframes with easing, letterbox bars and a skip button. Each shot lists a start CFrame, end CFrame, FOV and duration.

```lua
--!strict
-- ModuleScript: CutscenePlayer (client only)
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local TweenService = game:GetService("TweenService")

local CutscenePlayer = {}

export type Shot = {
	from: CFrame,
	to: CFrame,
	fovFrom: number?,
	fovTo: number?,
	duration: number,
	easing: Enum.EasingStyle?,
	direction: Enum.EasingDirection?,
}

local function makeGui(): (ScreenGui, Frame, Frame, TextButton)
	local gui = Instance.new("ScreenGui")
	gui.Name = "Cutscene"
	gui.IgnoreGuiInset = true
	gui.ResetOnSpawn = false
	gui.DisplayOrder = 100

	local top = Instance.new("Frame")
	top.BackgroundColor3 = Color3.new(0, 0, 0)
	top.BorderSizePixel = 0
	top.Size = UDim2.fromScale(1, 0.12)
	top.Position = UDim2.fromScale(0, -0.12)
	top.Parent = gui

	local bottom = top:Clone()
	bottom.AnchorPoint = Vector2.new(0, 0)
	bottom.Position = UDim2.fromScale(0, 1)
	bottom.Parent = gui

	local skip = Instance.new("TextButton")
	skip.Text = "Skip"
	skip.Size = UDim2.fromOffset(90, 36)
	skip.AnchorPoint = Vector2.new(1, 1)
	skip.Position = UDim2.new(1, -16, 1, -16)
	skip.BackgroundColor3 = Color3.fromRGB(30, 30, 30)
	skip.TextColor3 = Color3.new(1, 1, 1)
	skip.ZIndex = 5
	skip.Parent = gui

	return gui, top, bottom, skip
end

-- Plays shots in order. Returns true if finished, false if skipped.
function CutscenePlayer.play(shots: { Shot }, onShot: ((index: number) -> ())?): boolean
	local camera = workspace.CurrentCamera
	local playerGui = Players.LocalPlayer:WaitForChild("PlayerGui")
	local oldType, oldCFrame, oldFov = camera.CameraType, camera.CFrame, camera.FieldOfView

	local gui, top, bottom, skipButton = makeGui()
	gui.Parent = playerGui
	local barInfo = TweenInfo.new(0.4, Enum.EasingStyle.Quad, Enum.EasingDirection.Out)
	TweenService:Create(top, barInfo, { Position = UDim2.fromScale(0, 0) }):Play()
	TweenService:Create(bottom, barInfo, { Position = UDim2.fromScale(0, 0.88) }):Play()

	camera.CameraType = Enum.CameraType.Scriptable
	local skipped = false
	local skipConn = skipButton.Activated:Connect(function()
		skipped = true
	end)

	for i, shot in shots do
		if skipped then
			break
		end
		if onShot then
			onShot(i)
		end
		local fovA = shot.fovFrom or camera.FieldOfView
		local fovB = shot.fovTo or fovA
		local style = shot.easing or Enum.EasingStyle.Sine
		local dir = shot.direction or Enum.EasingDirection.InOut
		local elapsed = 0
		while elapsed < shot.duration and not skipped do
			elapsed += RunService.RenderStepped:Wait()
			local a = TweenService:GetValue(math.min(elapsed / shot.duration, 1), style, dir)
			camera.CFrame = shot.from:Lerp(shot.to, a)
			camera.FieldOfView = fovA + (fovB - fovA) * a
		end
	end

	skipConn:Disconnect()
	camera.CameraType = oldType
	camera.CFrame = oldCFrame
	camera.FieldOfView = oldFov
	gui:Destroy()
	return not skipped
end

return CutscenePlayer
```

Usage idea: build shots from parts in a folder (`from = camA.CFrame`, `to = camB.CFrame`). Hide other UI and freeze input before calling; restore after. `CFrame:Lerp` rotates along the shortest arc, which is fine for short shots. For curved fly-throughs, replace the lerp with a Bezier of position points.

## 7. CameraShake

```lua
--!strict
-- ModuleScript: CameraShake. Perlin-noise shake applied after the default camera update.
local RunService = game:GetService("RunService")

local CameraShake = {}
local active: { { amp: number, freq: number, t: number, dur: number, seed: number } } = {}
local connected = false

local function step(dt: number)
	local camera = workspace.CurrentCamera
	local offset = Vector3.zero
	local rot = Vector3.zero
	for i = #active, 1, -1 do
		local s = active[i]
		s.t += dt
		if s.t >= s.dur then
			table.remove(active, i)
		else
			local fade = 1 - s.t / s.dur
			local n = s.t * s.freq
			offset += Vector3.new(
				math.noise(n, s.seed, 0),
				math.noise(s.seed, n, 1),
				0
			) * s.amp * fade
			rot += Vector3.new(0, 0, math.noise(n, 7, s.seed)) * s.amp * fade * 0.05
		end
	end
	camera.CFrame = camera.CFrame * CFrame.new(offset) * CFrame.Angles(rot.X, rot.Y, rot.Z)
end

function CameraShake.shake(amplitude: number, frequency: number, duration: number)
	table.insert(active, { amp = amplitude, freq = frequency, t = 0, dur = duration, seed = math.random() * 100 })
	if not connected then
		connected = true
		-- Run after the default camera scripts so the shake is not overwritten.
		RunService:BindToRenderStep("CameraShakeStep", Enum.RenderPriority.Camera.Value + 1, step)
	end
end

return CameraShake
```

Binding at `Camera.Value + 1` follows DevForum advice on shake being overwritten. The step keeps running while idle; unbind when `#active == 0` for efficiency if desired.

## Related
[[Animation Principles for Roblox]] · [[Locomotion Walk Run Sprint]] · [[Cutscenes and Camera Work]] · [[Code Performance and Optimization]] · [[UI Implementation in Luau]]

## References

- [Use animations](https://create.roblox.com/docs/building-and-visuals/animation/using-animations) — docs · playing tracks
- [Animation events](https://create.roblox.com/docs/animation/events) — docs · marker pattern
- [AnimationTrack](https://create.roblox.com/docs/reference/engine/classes/AnimationTrack) — API · Play, signals
- [KeyframeMarker](https://create.roblox.com/docs/reference/engine/classes/KeyframeMarker) — API · marker instance
- [Play character animations](https://create.roblox.com/docs/en-us/tutorials/use-case-tutorials/animation/play-character-animations) — tutorial · scripted playback
- [IKControl (Italian page)](https://create.roblox.com/docs/it-it/reference/engine/classes/IKControl) — API · IK alternative for look-at
- [How to Create Camera Cutscenes](https://devforum.roblox.com/t/how-to-create-camera-cutscenes/1629318) — tutorial · cutscene structure
- [How do I skip a cutscene?](https://devforum.roblox.com/t/how-do-i-skip-a-cutscene/1192583) — forum · skip handling
- [Cutscene Instantly Jumps to the Next Tween Position](https://devforum.roblox.com/t/cutscene-instantly-jumps-to-the-next-tween-position/815219) — forum · tween waiting
- [Help with Camera Shake Module](https://devforum.roblox.com/t/help-with-camera-shake-module/2418949) — forum · render priority
- [Simple Shake](https://devforum.roblox.com/t/simple-shake-easy-camera-shake-module/4457496) — community · Perlin approach
- [EZ Camera Shake V2](https://devforum.roblox.com/t/ez-camera-shake-v2-a-refresh-of-a-popular-preferred-module-for-applying-camera-shake-effects/4671745) — community · reference module
- [Camera Manipulation (Spectate and Cutscenes) #32](https://www.youtube.com/watch?v=FhCNvyuZ-mE) — video · camera scripting
- [Cutscene Camera (Camera Interpolation)](https://www.youtube.com/watch?v=DQ0FbFJ0IU8) — video · interpolation
- [Trying to make a more smooth fishing rod cast](https://devforum.roblox.com/t/trying-to-make-a-more-smooth-fishing-rod-cast/2431891) — forum · Bezier motion idea
- [Replacing default Animate script with a custom one](https://devforum.roblox.com/t/replacing-default-animate-script-with-a-custom-one/2920725) — forum · controller replacement

Links: [[Animation MOC]] · [[00 Home]]
