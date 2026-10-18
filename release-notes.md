Manual test build of the playable PokeFields Android client with the mobile UI changes. This is a prerelease for manual installation and testing. It is not offered through the production automatic updater.

Installs separately as **PokeFields Mobile Test** (app.unofficial.pokefields.mobiletest). Import your ROMs and sign in again. No ROMs included. The standard app remains installed.

**Test 4 (1.0.11-mobiletest.4)** updates the existing separate test app. Keeps imported ROMs and settings when installed over Test 1 or Test 2.

**New in Test 4:** Chat stays on screen and shrinks to a live feed above open menus instead of disappearing. The original nine-slot hotbar and three presets are back in a movable/collapsible window. Drag its header to reposition it; positions are saved.

The outer Party window sits alongside Jobs. Minimize/maximize it with minus/plus, drag its header to move it, and drag a Pokemon onto another to reorder the real party. The Party shortcut toggles this window; tapping a Pokemon opens the existing action menu. Jobs and Encounters retain their native minimize/X controls with larger touch targets and movable headers.

GTL and Map replace Battle and Social in the bottom navigation. Battle and Social remain under Menu > More. Both inventory views have larger, separated up/down scroll buttons and a wider scrollbar; the full inventory also has larger item slots. Hold B for a moment, then drag it to move it independently, like the emote icon. B position is saved. Normal B use and dialogue A/B/D-pad behavior are retained.

Local source and compiled-pack checks cover chat visibility, all nine hotbar slots, header movement/persistence, physical party drag/reorder output, collapsible party, inventory scroll controls, independent B drag, and earlier dialogue/battle/menu behavior. No connected Android phone was available; live gameplay retesting remains necessary.

Mail now fills the phone screen with a scrolling inbox and compose form. Friends has a usable scrolling list, search, sorting and tap-to-open player menus. Matchmaking replaces its desktop sidebar with a section picker and large Ranked/Casual controls; server eligibility rules remain unchanged. HMs are under TMs/HMs, and exploration items are under Other.

Battle entry now reveals the fight window immediately rather than leaving the map visible while waiting for its first event batch. Overworld touch controls stop intercepting battle taps. Battle layout and move controls fit landscape phone sizes. This addresses the local transition/input problems; the reported live phone battle still needs retesting.

Source and actual compiled-pack checks passed with populated lists, queue eligibility, battle entry, move-button output and three landscape viewport sizes. Desktop renders inspected. No phone was connected through ADB; no live account action was performed. No ROMs included.

Automatic APK/resource updates are disabled inside this test app. The public stable release and signed update manifests are unchanged. Do not use this prerelease for a normal release rollout.

SHA-256: `de93efa09b8c28de4c15c068fa71684e33e35fb55bfb5120fa902d2bf4fb7d4d`
