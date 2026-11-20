---
title: UI Implementation in Luau
date: 2026-11-02
tags: [ui, luau, code, components]
status: untested
---

# UI Implementation in Luau

Original, typed reference modules for the UI patterns in this folder. **status: untested** — none of this has been run in Studio; test before shipping. All code is original and free to adapt. Design rationale: [[UI Design Principles for Roblox]], [[UI Animation and Juice]], [[Mobile Console and Responsive UI]]. Architecture context: [[Project Architecture and Frameworks]].

## Where things go
| Module | Location | Runs on |
|---|---|---|
| `Rarity` | ReplicatedStorage/UI/Rarity | client (shared data) |
| `NumberFormat` | ReplicatedStorage/UI/NumberFormat | client |
| `AnimatedButton` | ReplicatedStorage/UI/AnimatedButton | client |
| `CurrencyCounter` | ReplicatedStorage/UI/CurrencyCounter | client |
| `Popup` | ReplicatedStorage/UI/Popup | client |
| `Toasts` | ReplicatedStorage/UI/Toasts | client |
| `ShopGrid` | ReplicatedStorage/UI/ShopGrid | client |
| `RarityFrame` | ReplicatedStorage/UI/RarityFrame | client |
| `Responsive` | ReplicatedStorage/UI/Responsive | client |
| `PetPreview` | ReplicatedStorage/UI/PetPreview | client |
| Bootstrapping LocalScript | StarterPlayerScripts or StarterGui | client |

Never trust the client for currency or purchases; these modules only display. See [[Security and Anti-Exploit]].

---

## 1. Rarity data
```lua
--!strict
-- ReplicatedStorage/UI/Rarity
export type RarityInfo = {
	name: string,
	color: Color3,
	stroke: Color3,
	gradient: ColorSequence,
}

local function info(name: string, top: Color3, bottom: Color3, stroke: Color3): RarityInfo
	return {
		name = name,
		color = top,
		stroke = stroke,
		gradient = ColorSequence.new(top, bottom),
	}
end

local Rarity = {
	Common = info("Common", Color3.fromHex("#D5D8DE"), Color3.fromHex("#9AA0AB"), Color3.fromHex("#4A4F59")),
	Uncommon = info("Uncommon", Color3.fromHex("#7BE87B"), Color3.fromHex("#3FB04A"), Color3.fromHex("#1F6B2A")),
	Rare = info("Rare", Color3.fromHex("#62B4FF"), Color3.fromHex("#2D7BE0"), Color3.fromHex("#1B4A9C")),
	Epic = info("Epic", Color3.fromHex("#C687FF"), Color3.fromHex("#8A3FE0"), Color3.fromHex("#52209B")),
	Legendary = info("Legendary", Color3.fromHex("#FFD060"), Color3.fromHex("#F09A10"), Color3.fromHex("#9A5A00")),
	Mythic = info("Mythic", Color3.fromHex("#FF7A93"), Color3.fromHex("#E02A55"), Color3.fromHex("#8A1230")),
}

return Rarity
```

## 2. Number formatting
```lua
--!strict
-- ReplicatedStorage/UI/NumberFormat
local NumberFormat = {}

local SUFFIXES = { "", "K", "M", "B", "T", "Qa", "Qi", "Sx", "Sp", "Oc", "No", "Dc" }

local function trimZeros(s: string): string
	if string.find(s, ".", 1, true) then
		s = string.gsub(s, "0+$", "")
		s = string.gsub(s, "%.$", "")
	end
	return s
end

-- 999 -> "999", 1234 -> "1.2K", 3.4e6 -> "3.4M", 1.5e15 -> "1.5Qa"
function NumberFormat.abbreviate(value: number, decimals: number?): string
	local d = decimals or 1
	if value ~= value then
		return "0"
	end
	local sign = if value < 0 then "-" else ""
	local n = math.abs(value)
	if n < 1000 then
		return sign .. tostring(math.floor(n))
	end
	local idx = math.min(math.floor(math.log10(n) / 3), #SUFFIXES - 1)
	local scaled = n / (10 ^ (idx * 3))
	local mult = 10 ^ d
	scaled = math.floor(scaled * mult) / mult
	if scaled >= 1000 and idx < #SUFFIXES - 1 then
		idx += 1
		scaled /= 1000
	end
	return sign .. trimZeros(string.format("%." .. d .. "f", scaled)) .. SUFFIXES[idx + 1]
end

-- 1234567 -> "1,234,567"
function NumberFormat.commas(value: number): string
	local s = tostring(math.floor(value))
	local reversed = (string.gsub(string.reverse(s), "(%d%d%d)", "%1,"))
	local out = string.reverse(reversed)
	return (string.gsub(out, "^,", ""))
end

return NumberFormat
```

## 3. Animated button component
```lua
--!strict
-- ReplicatedStorage/UI/AnimatedButton
local TweenService = game:GetService("TweenService")

export type Options = {
	hoverScale: number?,
	pressScale: number?,
	onClick: (() -> ())?,
	-- Sound hook: kind is "hover" | "press" | "click". Wire to your audio module ([[UI Sounds]]).
	onSound: ((kind: string) -> ())?,
}

local AnimatedButton = {}
AnimatedButton.__index = AnimatedButton

export type Button = typeof(setmetatable(
	{} :: {
		_button: GuiButton,
		_scale: UIScale,
		_hover: number,
		_press: number,
		_isHover: boolean,
		_conns: { RBXScriptConnection },
		_opts: Options,
	},
	AnimatedButton
))

local HOVER_INFO = TweenInfo.new(0.1, Enum.EasingStyle.Quad, Enum.EasingDirection.Out)
local PRESS_INFO = TweenInfo.new(0.06, Enum.EasingStyle.Quad, Enum.EasingDirection.Out)
local RELEASE_INFO = TweenInfo.new(0.18, Enum.EasingStyle.Back, Enum.EasingDirection.Out)

function AnimatedButton.new(button: GuiButton, opts: Options?): Button
	local options: Options = opts or {}
	local scale = button:FindFirstChildOfClass("UIScale")
	if not scale then
		scale = Instance.new("UIScale")
		scale.Parent = button
	end

	local self = setmetatable({
		_button = button,
		_scale = scale :: UIScale,
		_hover = options.hoverScale or 1.06,
		_press = options.pressScale or 0.92,
		_isHover = false,
		_conns = {},
		_opts = options,
	}, AnimatedButton)

	local function tweenTo(target: number, info: TweenInfo)
		TweenService:Create(self._scale, info, { Scale = target }):Play()
	end
	local function sound(kind: string)
		if self._opts.onSound then
			self._opts.onSound(kind)
		end
	end

	table.insert(self._conns, button.MouseEnter:Connect(function()
		self._isHover = true
		sound("hover")
		tweenTo(self._hover, HOVER_INFO)
	end))
	table.insert(self._conns, button.MouseLeave:Connect(function()
		self._isHover = false
		tweenTo(1, HOVER_INFO)
	end))
	table.insert(self._conns, button.MouseButton1Down:Connect(function()
		sound("press")
		tweenTo(self._press, PRESS_INFO)
	end))
	table.insert(self._conns, button.MouseButton1Up:Connect(function()
		tweenTo(if self._isHover then self._hover else 1, RELEASE_INFO)
	end))
	table.insert(self._conns, button.Activated:Connect(function()
		sound("click")
		if self._opts.onClick then
			self._opts.onClick()
		end
	end))

	return self
end

function AnimatedButton.Destroy(self: Button)
	for _, c in self._conns do
		c:Disconnect()
	end
	table.clear(self._conns)
end

return AnimatedButton
```
Note: on touch there is no hover; the press/release tweens carry the feedback.

## 4. Currency counter with count-up
```lua
--!strict
-- ReplicatedStorage/UI/CurrencyCounter
local TweenService = game:GetService("TweenService")
local NumberFormat = require(script.Parent.NumberFormat)

local CurrencyCounter = {}
CurrencyCounter.__index = CurrencyCounter

export type Counter = typeof(setmetatable(
	{} :: {
		_label: TextLabel,
		_value: NumberValue,
		_prefix: string,
		_conn: RBXScriptConnection,
		_tween: Tween?,
	},
	CurrencyCounter
))

function CurrencyCounter.new(label: TextLabel, startValue: number, prefix: string?): Counter
	local value = Instance.new("NumberValue")
	value.Value = startValue
	local self = setmetatable({
		_label = label,
		_value = value,
		_prefix = prefix or "",
		_tween = nil,
	}, CurrencyCounter) :: any

	local function render()
		label.Text = self._prefix .. NumberFormat.abbreviate(value.Value, 2)
	end
	self._conn = value.Changed:Connect(render)
	render()
	return self
end

-- Retargets smoothly even if a previous tween is still running.
function CurrencyCounter.set(self: Counter, target: number, duration: number?)
	if self._tween then
		self._tween:Cancel()
	end
	local t = TweenService:Create(
		self._value,
		TweenInfo.new(duration or 0.5, Enum.EasingStyle.Quart, Enum.EasingDirection.Out),
		{ Value = target }
	)
	self._tween = t
	t:Play()
end

function CurrencyCounter.Destroy(self: Counter)
	self._conn:Disconnect()
	if self._tween then
		self._tween:Cancel()
	end
	self._value:Destroy()
end

return CurrencyCounter
```
Usage: `local c = CurrencyCounter.new(gui.Coins.Amount, 0); remote.OnClientEvent:Connect(function(n) c:set(n) end)`.

## 5. Popup open/close with tween and blur
```lua
--!strict
-- ReplicatedStorage/UI/Popup
local TweenService = game:GetService("TweenService")

local Popup = {}
Popup.__index = Popup

export type PopupObj = typeof(setmetatable(
	{} :: {
		_frame: GuiObject,
		_scale: UIScale,
		_blur: BlurEffect,
		_open: boolean,
		_blurSize: number,
	},
	Popup
))

local OPEN_INFO = TweenInfo.new(0.3, Enum.EasingStyle.Back, Enum.EasingDirection.Out)
local CLOSE_INFO = TweenInfo.new(0.18, Enum.EasingStyle.Quad, Enum.EasingDirection.In)

function Popup.new(frame: GuiObject, blurSize: number?): PopupObj
	local scale = frame:FindFirstChildOfClass("UIScale")
	if not scale then
		scale = Instance.new("UIScale")
		scale.Parent = frame
	end
	-- One blur per popup, parented to the camera so only this player sees it.
	local blur = Instance.new("BlurEffect")
	blur.Size = 0
	blur.Enabled = false
	blur.Parent = workspace.CurrentCamera

	frame.Visible = false
	return setmetatable({
		_frame = frame,
		_scale = scale :: UIScale,
		_blur = blur,
		_open = false,
		_blurSize = blurSize or 16,
	}, Popup)
end

function Popup.open(self: PopupObj)
	if self._open then
		return
	end
	self._open = true
	self._scale.Scale = 0.85
	self._frame.Visible = true
	self._blur.Enabled = true
	TweenService:Create(self._scale, OPEN_INFO, { Scale = 1 }):Play()
	TweenService:Create(self._blur, OPEN_INFO, { Size = self._blurSize }):Play()
end

function Popup.close(self: PopupObj)
	if not self._open then
		return
	end
	self._open = false
	local t1 = TweenService:Create(self._scale, CLOSE_INFO, { Scale = 0.85 })
	local t2 = TweenService:Create(self._blur, CLOSE_INFO, { Size = 0 })
	t1:Play()
	t2:Play()
	t1.Completed:Once(function()
		if not self._open then
			self._frame.Visible = false
			self._blur.Enabled = false
		end
	end)
end

function Popup.toggle(self: PopupObj)
	if self._open then
		self:close()
	else
		self:open()
	end
end

function Popup.Destroy(self: PopupObj)
	self._blur:Destroy()
end

return Popup
```

## 6. Notification toast queue
```lua
--!strict
-- ReplicatedStorage/UI/Toasts
local TweenService = game:GetService("TweenService")

local Toasts = {}
Toasts.__index = Toasts

export type ToastData = { text: string, color: Color3?, duration: number? }

export type ToastHost = typeof(setmetatable(
	{} :: {
		_container: GuiObject,
		_queue: { ToastData },
		_active: number,
		_max: number,
	},
	Toasts
))

-- container should hold a UIListLayout (bottom-aligned or top-aligned).
function Toasts.new(container: GuiObject, maxVisible: number?): ToastHost
	return setmetatable({
		_container = container,
		_queue = {},
		_active = 0,
		_max = maxVisible or 3,
	}, Toasts)
end

local function build(data: ToastData): Frame
	local f = Instance.new("Frame")
	f.Size = UDim2.fromScale(1, 0)
	f.AutomaticSize = Enum.AutomaticSize.Y
	f.BackgroundColor3 = data.color or Color3.fromHex("#2B2D5B")
	f.BackgroundTransparency = 1

	local corner = Instance.new("UICorner")
	corner.CornerRadius = UDim.new(0, 12)
	corner.Parent = f

	local stroke = Instance.new("UIStroke")
	stroke.Thickness = 3
	stroke.Color = Color3.fromHex("#101018")
	stroke.Transparency = 1
	stroke.Parent = f

	local pad = Instance.new("UIPadding")
	pad.PaddingLeft = UDim.new(0, 12)
	pad.PaddingRight = UDim.new(0, 12)
	pad.PaddingTop = UDim.new(0, 8)
	pad.PaddingBottom = UDim.new(0, 8)
	pad.Parent = f

	local label = Instance.new("TextLabel")
	label.BackgroundTransparency = 1
	label.Size = UDim2.fromScale(1, 0)
	label.AutomaticSize = Enum.AutomaticSize.Y
	label.FontFace = Font.fromEnum(Enum.Font.FredokaOne)
	label.TextSize = 22
	label.TextColor3 = Color3.new(1, 1, 1)
	label.TextTransparency = 1
	label.TextWrapped = true
	label.Text = data.text
	label.Parent = f

	local labelStroke = Instance.new("UIStroke")
	labelStroke.Thickness = 2
	labelStroke.Color = Color3.fromHex("#101018")
	labelStroke.Transparency = 1
	labelStroke.Parent = label

	return f
end

local function fade(f: Frame, to: number, info: TweenInfo)
	TweenService:Create(f, info, { BackgroundTransparency = to }):Play()
	for _, d in f:GetDescendants() do
		if d:IsA("TextLabel") then
			TweenService:Create(d, info, { TextTransparency = to }):Play()
		elseif d:IsA("UIStroke") then
			TweenService:Create(d, info, { Transparency = to }):Play()
		end
	end
	local s = f:FindFirstChildOfClass("UIStroke")
	if s then
		TweenService:Create(s, info, { Transparency = to }):Play()
	end
end

function Toasts._pump(self: ToastHost)
	while self._active < self._max and #self._queue > 0 do
		local data = table.remove(self._queue, 1) :: ToastData
		self._active += 1
		local f = build(data)
		f.Parent = self._container
		fade(f, 0, TweenInfo.new(0.25, Enum.EasingStyle.Quint, Enum.EasingDirection.Out))
		task.delay(data.duration or 3, function()
			fade(f, 1, TweenInfo.new(0.25, Enum.EasingStyle.Quad, Enum.EasingDirection.In))
			task.wait(0.3)
			f:Destroy()
			self._active -= 1
			self:_pump()
		end)
	end
end

function Toasts.push(self: ToastHost, data: ToastData)
	table.insert(self._queue, data)
	self:_pump()
end

return Toasts
```
Hook a server notification RemoteEvent to `toasts:push({ text = msg })` in a LocalScript.

## 7. Shop grid from data
```lua
--!strict
-- ReplicatedStorage/UI/ShopGrid
local Rarity = require(script.Parent.Rarity)
local NumberFormat = require(script.Parent.NumberFormat)

export type ShopItem = {
	id: string,
	name: string,
	price: number,
	rarity: string, -- key in Rarity
	icon: string, -- rbxassetid:// string you own
}

local ShopGrid = {}

-- parent must be a ScrollingFrame. Returns a cleanup function.
function ShopGrid.build(parent: ScrollingFrame, items: { ShopItem }, onBuy: (ShopItem) -> ()): () -> ()
	parent.AutomaticCanvasSize = Enum.AutomaticSize.Y
	parent.CanvasSize = UDim2.new()

	local grid = parent:FindFirstChildOfClass("UIGridLayout")
	if not grid then
		grid = Instance.new("UIGridLayout")
		grid.Parent = parent
	end
	grid.CellSize = UDim2.fromOffset(150, 190)
	grid.CellPadding = UDim2.fromOffset(10, 10)
	grid.SortOrder = Enum.SortOrder.LayoutOrder

	local conns: { RBXScriptConnection } = {}
	local cards: { Frame } = {}

	for i, item in items do
		local style = Rarity[item.rarity] or Rarity.Common

		local card = Instance.new("Frame")
		card.Name = item.id
		card.LayoutOrder = i
		card.BackgroundColor3 = Color3.new(1, 1, 1)

		local corner = Instance.new("UICorner")
		corner.CornerRadius = UDim.new(0, 14)
		corner.Parent = card

		local g = Instance.new("UIGradient")
		g.Color = style.gradient
		g.Rotation = 90
		g.Parent = card

		local stroke = Instance.new("UIStroke")
		stroke.Thickness = 3
		stroke.Color = style.stroke
		stroke.Parent = card

		local icon = Instance.new("ImageLabel")
		icon.BackgroundTransparency = 1
		icon.Image = item.icon
		icon.Size = UDim2.fromScale(0.7, 0.5)
		icon.Position = UDim2.fromScale(0.15, 0.06)
		icon.ScaleType = Enum.ScaleType.Fit
		icon.Parent = card

		local name = Instance.new("TextLabel")
		name.BackgroundTransparency = 1
		name.Size = UDim2.fromScale(0.9, 0.16)
		name.Position = UDim2.fromScale(0.05, 0.58)
		name.Text = item.name
		name.TextScaled = true
		name.FontFace = Font.fromEnum(Enum.Font.FredokaOne)
		name.TextColor3 = Color3.new(1, 1, 1)
		name.Parent = card
		local nameStroke = Instance.new("UIStroke")
		nameStroke.Thickness = 2
		nameStroke.Color = Color3.fromHex("#101018")
		nameStroke.Parent = name

		local buy = Instance.new("TextButton")
		buy.Size = UDim2.fromScale(0.84, 0.18)
		buy.Position = UDim2.fromScale(0.08, 0.77)
		buy.BackgroundColor3 = Color3.fromHex("#3DDC4E")
		buy.Text = NumberFormat.abbreviate(item.price)
		buy.TextScaled = true
		buy.FontFace = Font.fromEnum(Enum.Font.FredokaOne)
		buy.TextColor3 = Color3.new(1, 1, 1)
		buy.Parent = card
		local bc = Instance.new("UICorner")
		bc.CornerRadius = UDim.new(0, 10)
		bc.Parent = buy
		local bs = Instance.new("UIStroke")
		bs.Thickness = 2
		bs.Color = Color3.fromHex("#1B6B25")
		bs.Parent = buy

		table.insert(conns, buy.Activated:Connect(function()
			onBuy(item)
		end))

		card.Parent = parent
		table.insert(cards, card)
	end

	return function()
		for _, c in conns do
			c:Disconnect()
		end
		for _, card in cards do
			card:Destroy()
		end
	end
end

return ShopGrid
```
`onBuy` should fire a RemoteEvent; the server validates and calls MarketplaceService when needed ([[Shop and Monetization UI]]).

## 8. Rarity gradient frame with rotating shine
```lua
--!strict
-- ReplicatedStorage/UI/RarityFrame
local TweenService = game:GetService("TweenService")
local Rarity = require(script.Parent.Rarity)

local RarityFrame = {}

-- Adds gradient fill, white stroke carrying a rotating gradient, and a diagonal shine sweep.
-- Returns a cleanup function that stops the loops.
function RarityFrame.apply(frame: GuiObject, rarityName: string, animated: boolean?): () -> ()
	local style = Rarity[rarityName] or Rarity.Common
	frame.BackgroundColor3 = Color3.new(1, 1, 1)

	local fill = Instance.new("UIGradient")
	fill.Name = "RarityFill"
	fill.Color = style.gradient
	fill.Rotation = 90
	fill.Parent = frame

	local stroke = Instance.new("UIStroke")
	stroke.Name = "RarityStroke"
	stroke.Thickness = 3
	stroke.Color = Color3.new(1, 1, 1) -- must be white for the gradient to show
	stroke.Parent = frame

	local strokeGrad = Instance.new("UIGradient")
	strokeGrad.Color = ColorSequence.new(style.color, style.stroke)
	strokeGrad.Parent = stroke

	local tweens: { Tween } = {}
	local shine: Frame? = nil

	if animated then
		-- Rotating border
		local spin = TweenService:Create(
			strokeGrad,
			TweenInfo.new(3, Enum.EasingStyle.Linear, Enum.EasingDirection.InOut, -1),
			{ Rotation = 360 }
		)
		spin:Play()
		table.insert(tweens, spin)

		-- Shine sweep overlay
		local s = Instance.new("Frame")
		s.Name = "Shine"
		s.Size = UDim2.fromScale(1, 1)
		s.BackgroundColor3 = Color3.new(1, 1, 1)
		s.BorderSizePixel = 0
		s.ZIndex = frame.ZIndex + 5
		local sc = Instance.new("UICorner")
		sc.CornerRadius = UDim.new(0, 14)
		sc.Parent = s
		local sg = Instance.new("UIGradient")
		sg.Rotation = 25
		sg.Transparency = NumberSequence.new({
			NumberSequenceKeypoint.new(0, 1),
			NumberSequenceKeypoint.new(0.45, 1),
			NumberSequenceKeypoint.new(0.5, 0.55),
			NumberSequenceKeypoint.new(0.55, 1),
			NumberSequenceKeypoint.new(1, 1),
		})
		sg.Offset = Vector2.new(-1, 0)
		sg.Parent = s
		s.Parent = frame
		shine = s

		local sweep = TweenService:Create(
			sg,
			TweenInfo.new(1.4, Enum.EasingStyle.Sine, Enum.EasingDirection.InOut, -1, false, 0.8),
			{ Offset = Vector2.new(1, 0) }
		)
		sweep:Play()
		table.insert(tweens, sweep)
	end

	return function()
		for _, t in tweens do
			t:Cancel()
		end
		if shine then
			shine:Destroy()
		end
	end
end

return RarityFrame
```
Shine overlays on `CanvasGroup` parents clip cleanly; otherwise keep the same UICorner radius on the overlay.

## 9. Responsive scaling helper
```lua
--!strict
-- ReplicatedStorage/UI/Responsive
local Responsive = {}

local REF = Vector2.new(1920, 1080)

-- Attach to a ScreenGui. Design all children at 1920x1080 in Offset or Scale.
function Responsive.bind(gui: ScreenGui, minScale: number?, maxScale: number?): () -> ()
	gui.ScreenInsets = Enum.ScreenInsets.CoreUISafeInsets

	local scale = gui:FindFirstChildOfClass("UIScale")
	if not scale then
		scale = Instance.new("UIScale")
		scale.Parent = gui
	end
	local lo = minScale or 0.5
	local hi = maxScale or 1.5

	local function update()
		local cam = workspace.CurrentCamera
		if not cam then
			return
		end
		local vp = cam.ViewportSize
		local s = math.min(vp.X / REF.X, vp.Y / REF.Y)
		(scale :: UIScale).Scale = math.clamp(s, lo, hi)
	end

	update()
	local conn = (workspace.CurrentCamera :: Camera):GetPropertyChangedSignal("ViewportSize"):Connect(update)
	return function()
		conn:Disconnect()
	end
end

-- True on touch-first devices; use to swap layouts.
function Responsive.isTouch(): boolean
	local UIS = game:GetService("UserInputService")
	return UIS.TouchEnabled and not UIS.KeyboardEnabled
end

return Responsive
```
Caveat: a ScreenGui-level UIScale shrinks everything on phones; combine with a floor (`minScale`) and larger designs for small screens. Review the touch-size guidance in [[Mobile Console and Responsive UI]].

## 10. ViewportFrame pet preview
```lua
--!strict
-- ReplicatedStorage/UI/PetPreview
local RunService = game:GetService("RunService")

local PetPreview = {}

-- Shows a clone of `model` in `viewport`, slowly rotating. Returns cleanup.
function PetPreview.show(viewport: ViewportFrame, model: Model): () -> ()
	viewport:ClearAllChildren()
	viewport.BackgroundTransparency = 1
	viewport.Ambient = Color3.fromRGB(200, 200, 200)
	viewport.LightColor = Color3.fromRGB(255, 255, 255)

	local world = Instance.new("WorldModel") -- lets animations/physics run inside the viewport
	world.Parent = viewport

	local clone = model:Clone()
	clone.Parent = world
	local _, size = clone:GetBoundingBox()
	clone:PivotTo(CFrame.new())

	local cam = Instance.new("Camera")
	cam.FieldOfView = 40
	viewport.CurrentCamera = cam
	cam.Parent = viewport

	local radius = size.Magnitude * 0.5
	local dist = radius / math.tan(math.rad(cam.FieldOfView / 2)) * 1.1
	local target = Vector3.zero
	local angle = 0

	local conn = RunService.Heartbeat:Connect(function(dt)
		angle += dt * 0.8
		clone:PivotTo(CFrame.new() * CFrame.Angles(0, angle, 0))
		cam.CFrame = CFrame.lookAt(Vector3.new(0, size.Y * 0.2, dist), target)
	end)

	return function()
		conn:Disconnect()
		clone:Destroy()
		cam:Destroy()
		world:Destroy()
	end
end

return PetPreview
```
Known limits: fixed lighting, no particles/shadows in ViewportFrames, and cameras must be assigned per viewport ([release post](https://devforum.roblox.com/t/viewportframe-release/206476)). The bounding-box target math is simplistic; re-centre pivots in your pet models. For a fuller module see [Module3D thread](https://devforum.roblox.com/t/how-to-render-viewportframe-in-surfacegui/2656759).

## Bootstrap example
```lua
--!strict
-- StarterPlayerScripts/UIBootstrap (LocalScript)
local RS = game:GetService("ReplicatedStorage")
local Players = game:GetService("Players")
local UI = RS:WaitForChild("UI")
local Responsive = require(UI.Responsive)
local Toasts = require(UI.Toasts)

local gui = Players.LocalPlayer:WaitForChild("PlayerGui"):WaitForChild("MainHud") :: ScreenGui
Responsive.bind(gui)
local host = Toasts.new(gui:WaitForChild("ToastHost") :: GuiObject, 3)
host:push({ text = "Welcome!" })
```

## Testing checklist
- [ ] Run each module in an empty place with a sample frame.
- [ ] Verify no leaked tweens after `Destroy`.
- [ ] Verify abbreviation at 999, 1000, 999999, 1e15, 1e40.
- [ ] Test on emulated phone, tablet, desktop.

## References
- [TweenService easing styles](https://create.roblox.com/docs/en-us/reference/engine/enums/EasingStyle.md) — official docs · easing used above
- [UI appearance modifiers](https://create.roblox.com/docs/en-us/ui/appearance-modifiers) — official docs · UIStroke/UIGradient/UICorner
- [Size modifiers and constraints](https://create.roblox.com/docs/en-us/ui/size-modifiers) — official docs · UIScale
- [ScreenInsets enum](https://create.roblox.com/docs/en-us/reference/engine/enums/ScreenInsets.md) — official docs · CoreUISafeInsets
- [UIGridLayout](https://create.roblox.com/docs/en-us/reference/engine/classes/UIGridLayout.md) — official docs · shop grid
- [Font datatype](https://create.roblox.com/docs/en-us/reference/engine/datatypes/Font.md) — official docs · Font.fromEnum
- [ViewportFrame Release](https://devforum.roblox.com/t/viewportframe-release/206476) — DevForum · limits
- [How to render viewportframe in surfacegui](https://devforum.roblox.com/t/how-to-render-viewportframe-in-surfacegui/2656759) — DevForum · Module3D pointer
- [A Question on Viewport Frames](https://devforum.roblox.com/t/a-question-on-viewport-frames/385060) — DevForum · camera setup
- [ViewPort frame not rendering?](https://devforum.roblox.com/t/viewport-frame-not-rendering/2697680) — DevForum · troubleshooting
- [3D rotating viewport not working](https://devforum.roblox.com/t/3d-rotating-viewport-not-working/402729) — DevForum · rotation loops
- [UIGradient animation](https://devforum.roblox.com/t/uigradient-animation/2637300) — DevForum · shine technique
- [How to add a UIGradient into a gui border](https://devforum.roblox.com/t/how-to-add-a-uigradient-into-a-gui-border/1783385) — DevForum · white stroke + gradient
- [FormatNumber module](https://devforum.roblox.com/t/311-formatnumber-a-module-for-formatting-numbers/527979) — DevForum · alternative number formatter
- [UI Blurred Background](https://devforum.roblox.com/t/ui-blurred-background/1088080) — DevForum · blur on popups

Links: [[UI MOC]] · [[00 Home]]
