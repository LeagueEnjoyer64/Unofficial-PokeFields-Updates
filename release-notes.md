Manual test build of the playable PokeFields Android client with the mobile UI changes. This is a prerelease for manual installation and testing. It is not offered through the production automatic updater.

Installs separately as **PokeFields Mobile Test** (app.unofficial.pokefields.mobiletest). Import your ROMs and sign in again. No ROMs included. The standard app remains installed.

**Test 2 (1.0.11-mobiletest.2)** updates the existing separate test app. Keeps imported ROMs and settings when installed over Test 1.

Mail now fills the phone screen with a scrolling inbox and compose form. Friends has a usable scrolling list, search, sorting and tap-to-open player menus. Matchmaking replaces its desktop sidebar with a section picker and large Ranked/Casual controls; server eligibility rules remain unchanged. HMs are under TMs/HMs, and exploration items are under Other.

Battle entry now reveals the fight window immediately rather than leaving the map visible while waiting for its first event batch. Overworld touch controls stop intercepting battle taps. Battle layout and move controls fit landscape phone sizes. This addresses the local transition/input problems; the reported live phone battle still needs retesting.

Source and actual compiled-pack checks passed with populated lists, queue eligibility, battle entry, move-button output and three landscape viewport sizes. Desktop renders inspected. No phone was connected through ADB; no live account action was performed. No ROMs included.

Automatic APK/resource updates are disabled inside this test app. The public stable release and signed update manifests are unchanged. Do not use this prerelease for a normal release rollout.

SHA-256: `71cdd86ab469647373de6fdf90043f05ac2696701d957f03b7767aa6d3d2eae1`
