Manual-install mobile UI test APK. This prerelease is not offered by the production automatic updater.

**Test 7 (1.0.11-mobiletest.7)** installs over the separate **PokeFields Mobile Test** app and retains its imported ROMs and settings. Package: app.unofficial.pokefields.mobiletest. No ROMs included.

**New in Test 7:**
- Party is hidden by default. Tap the bottom Party button to show or hide the vertical list. Removed its plus/minus/X buttons; no collapsed Party box is left on screen. Original Pokemon reorder/actions remain available when open.
- Status is transparent white text, permanently anchored at the top right with no panel/header, collapse buttons or drag handle. It always shows real location, money, game time and weather; stale saved collapse/positions are ignored.
- The full nine-slot hotbar stays locked at the top center with no header or plus/minus controls. Its item slots and three presets remain functional.
- Chat now actually hides when closed. A small Chat button reopens the original chat, preserving messages and input. Refresh no longer forces a closed chat back on screen.

Retains Test 6's pixel-edged gold/slate D-pad and A/B skin, control settings and all earlier menu fixes. Production updates remain disabled.

Local source and actual compiled-pack checks cover touch/mouse header capture, position retention after layout refresh, vertical party and original reorder output, live status values, compact chat dragging, inventory controls, dialogue A/B/D-pad, battle entry and three landscape viewport sizes. Desktop rendering inspected. Local regression checks passed; Android installation and visible HUD/chat checks are also performed over ADB.

Automatic APK/resource updates are disabled in this test app. The production release, main branch and signed update manifests remain unchanged.

SHA-256: `c7338363b06b86b1365be5004774f4c05d1b48c1ba8c3c2d42ef9964bb07baeb`
