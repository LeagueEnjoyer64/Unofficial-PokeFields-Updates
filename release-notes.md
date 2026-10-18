Manual-install mobile UI test APK. This prerelease is not offered by the production automatic updater.

**Test 6 (1.0.11-mobiletest.6)** installs over the separate **PokeFields Mobile Test** app and retains its imported ROMs and settings. Package: app.unofficial.pokefields.mobiletest. No ROMs included.

**New control skin:** custom pixel-edged dark slate D-pad and octagonal A/B buttons, gold borders, cream pixel glyphs, muted red A and green B accents. Pressed directions/buttons highlight immediately. Existing touch hit regions, control sizing, opacity, saved positions, multitouch and independent B dragging are retained.

- Native menus, confirmation/dialogue panels, battle window, custom mobile menus and HUD windows support touch dragging. Drag the title/header; panels without a header have a Move handle. Pointer capture continues outside the header. Layout refreshes no longer recenter moved menus.
- Party is a vertical list with its existing reorder actions, minimize/restore and close controls.
- One movable Status card groups the real location, money, current game time and weather. Time uses the game clock; weather follows the original HUD's game data.
- Compact chat has a drag handle and keeps its position during refresh. Jobs/Encounter visibility follows the world HUD, preserving their native visibility settings while avoiding dialogue-control interception.

Retains Test 4's nine-slot movable hotbar, persistent chat, GTL/Map shortcuts, larger inventory scrolling controls and independent B positioning. Original dialogue A/B/D-pad and battle touch behavior are retained.

Local source and actual compiled-pack checks cover touch/mouse header capture, position retention after layout refresh, vertical party and original reorder output, live status values, compact chat dragging, inventory controls, dialogue A/B/D-pad, battle entry and three landscape viewport sizes. Desktop rendering inspected. Phone gameplay testing is still required; no live account actions were performed.

Automatic APK/resource updates are disabled in this test app. The production release, main branch and signed update manifests remain unchanged.

SHA-256: `25c557b55f1516b3f30eae7c8a50d539982c7d261a6e50d2a71af475c1aefdec`
