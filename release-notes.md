Manual-install mobile UI test APK. This prerelease is not offered by the production automatic updater.

**Test 8 (1.0.11-mobiletest.8)** installs over the separate **PokeFields Mobile Test** app and retains its imported ROMs and settings. Package: app.unofficial.pokefields.mobiletest. No ROMs included.

**Test 8:**
- Map shortcut automatically selects an eligible party Pokemon with Fly and requests the normal server-authorized Fly map. Choose a visited Fly destination to travel. Existing HM, location, activity and server unlock rules remain in force; denied Fly falls back to viewing the map.
- PC-style compact HUD: borderless translucent hotbar slots, slim vertical Pokemon strip, no bulky outer panels or Party title. Larger mobile tap targets retained; Pokemon/item artwork remains clear.
- Fixed emote selections being suppressed after the picker closed while the HUD was still hidden. Icon artwork is centered in its button.
- Emote button is larger (60px) and opens a mobile grid with all seven client-supported emotes, large illustrated tiles, close/outside dismiss and proper movement blocking.
- Bottom navigation no longer retains focus or hover highlighting after a phone tap.
- Removed the 1/2/3 preset row. Hotbar rail and slot backgrounds are more transparent, retaining full-opacity item icons and readable quantities.
- Party is hidden by default. Tap the bottom Party button to show or hide the vertical list. Removed its plus/minus/X buttons; no collapsed Party box is left on screen. Original Pokemon reorder/actions remain available when open.
- Status reuses the original PokeFields stats widget and native colors: revision, optional FPS, ping, game time, weather, location, gold money and active field/repel details. It stays transparent and pinned top-right without chrome or dragging; stale saved collapse/positions are ignored.
- The full nine-slot hotbar stays locked at the top center with no header or plus/minus controls. Its nine item bindings remain functional; the desktop preset selectors are hidden.
- Chat now actually hides when closed. A small Chat button reopens the original chat, preserving messages and input. Refresh no longer forces a closed chat back on screen.

Retains Test 6's pixel-edged gold/slate D-pad and A/B skin, control settings and all earlier menu fixes. Production updates remain disabled.

Local source and actual compiled-pack checks cover touch/mouse header capture, position retention after layout refresh, vertical party and original reorder output, live status values, compact chat dragging, inventory controls, dialogue A/B/D-pad, battle entry and three landscape viewport sizes. Desktop rendering inspected. Local regression checks passed; Android installation and visible HUD/chat checks are also performed over ADB.

Automatic APK/resource updates are disabled in this test app. The production release, main branch and signed update manifests remain unchanged.

SHA-256: `900a6c4aa98e19b24bce8e636a80f670dc2dd49b8af3faa93a101ea3afc64827`
