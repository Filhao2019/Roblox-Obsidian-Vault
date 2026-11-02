---
title: Notifications Popups and Rewards
date: 2026-11-02
tags: [ui, notifications, popups, rewards]
status: researched
---

# Notifications Popups and Rewards

Transient UI: toasts, modals, reward reveals. Sounds in [[UI Sounds]]; effects in [[Reward and Rarity VFX]]; code in [[UI Implementation in Luau]].

## Types
| Type | Behaviour | Example |
|---|---|---|
| Toast | Small, stacked, auto-dismiss 2-5 s | "Not enough coins" |
| Banner | Wide strip top/centre, 3-6 s | Event started, server announcements |
| Modal popup | Dims/blurs world, needs a button | Shop, confirm sell |
| Reward reveal | Full-screen moment, item pops with rarity colour | [[Pet Simulator 99]] hatch, [[Sols RNG]] aura roll |
| Floating text | World-space number that rises and fades | Damage, +cash |
| Badge/dot | Red dot on a menu button | New item |

## Roblox default notifications
`StarterGui:SetCore("SendNotification", ...)` takes Title, Text, Icon, Duration (about 5 s default per forum reports) and a Callback that should be a BindableFunction ([help thread](https://devforum.roblox.com/t/sendnotification-help/2796954)). Reliability issues have been reported ([thread](https://devforum.roblox.com/t/setcore-notifications-broken/372693), [CoreGui thread](https://devforum.roblox.com/t/coregui-notification-not-working/704628)). Most top games build custom toasts for brand consistency; community modules exist ([Notification Service](https://devforum.roblox.com/t/notification-service/798241), [Apprise](https://devforum.roblox.com/t/apprise-notification-system/1381697)).

## Modal with blur
Open: show frame, tween UIScale 0.85 to 1 with Back Out, tween BlurEffect.Size 0 to ~16. Close in reverse. Parent the blur to `workspace.CurrentCamera` from a LocalScript so only that player is affected and avoid creating duplicates ([blur thread](https://devforum.roblox.com/t/need-help-with-a-script/1533951) and [UI blurred background](https://devforum.roblox.com/t/ui-blurred-background/1088080)). Modules: [BlurUI](https://devforum.roblox.com/t/blurui-blur-your-uis/1276408), [Objectual UI Blur](https://devforum.roblox.com/t/objectual-ui-blur/3626057).

## Reward reveal recipe
1. Dim the screen, hide competing HUD.
2. Shake/rattle the container (egg, roll orb) for 0.5-1.5 s.
3. Pop item with overshoot scale, rarity glow, name with stroke.
4. Rarer = longer, louder, more particles; offer "skip" for repeat players (Sols RNG guides mention skip/animation settings, see [guide](https://rblxguide.com/games/sols-rng/updates/beginners-guide)).
5. Auto-collect or click to dismiss.

## Rules
- Never stack more than 3-4 toasts; queue the rest.
- One modal at a time; clicking the dim area closes non-critical ones.
- Don't block gameplay in dangerous modes ([[Rivals]], [[Blade Ball]]).
- Always provide an escape for gamepad ([[Mobile Console and Responsive UI]]).

## References
- [SendNotification HELP](https://devforum.roblox.com/t/sendnotification-help/2796954) — DevForum · callback type
- [SetCore notifications broken](https://devforum.roblox.com/t/setcore-notifications-broken/372693) — DevForum · known issues
- [CoreGui notification not working](https://devforum.roblox.com/t/coregui-notification-not-working/704628) — DevForum · script placement
- [Notification Service](https://devforum.roblox.com/t/notification-service/798241) — DevForum resource · custom notifications
- [Apprise notification system](https://devforum.roblox.com/t/apprise-notification-system/1381697) — DevForum resource · toast module
- [Need help with a script (blur)](https://devforum.roblox.com/t/need-help-with-a-script/1533951) — DevForum · duplicate blur fix
- [UI Blurred Background](https://devforum.roblox.com/t/ui-blurred-background/1088080) — DevForum · blur approach
- [Blur Effects for UI Elements](https://devforum.roblox.com/t/blur-effects-for-ui-elements/359498) — DevForum · alternatives
- [Why doesn't Blur work?](https://devforum.roblox.com/t/why-doesnt-blur-work/1141098) — DevForum · troubleshooting
- [BlurUI](https://devforum.roblox.com/t/blurui-blur-your-uis/1276408) — DevForum resource · older blur module
- [Objectual UI Blur](https://devforum.roblox.com/t/objectual-ui-blur/3626057) — DevForum resource · newer blur module
- [UI Design help (background)](https://devforum.roblox.com/t/ui-design-help-background/2886016) — DevForum · translucent panels
- [Sols RNG beginners guide](https://rblxguide.com/games/sols-rng/updates/beginners-guide) — guide · skip/filters settings
- [Sol's RNG auto roll](https://allthings.how/sol-s-rng-how-to-get-auto-roll-and-quick-roll-in-roblox/) — guide · roll UI

Links: [[UI MOC]] · [[00 Home]]
