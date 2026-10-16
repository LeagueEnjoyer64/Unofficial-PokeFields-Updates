# Unofficial PokeFields Android updates

[Download the latest APK](https://github.com/LeagueEnjoyer64/Unofficial-PokeFields-Updates/releases/latest)

This is an unofficial Android port, not made by PokeFields. Report port-specific bugs to Tendo in the PokeFields Discord.

This repository contains downloads, signed update manifests, and release automation. It does not contain the editable game project, ROMs, account credentials, or signing keys. Application binaries can still be reverse-engineered.

Install APK updates over the existing unofficial app to retain imported ROMs and settings. Version 1.0.9 adds full APK updates inside the app. Users on older versions need to install v1.0.9 once to enable this feature.

Compatible resource fixes download automatically; after verification the app displays a three-second notice and restarts. When a new APK is needed, the app offers to download it, verifies its release signature, checksum, package identity and Android signing certificate, and opens Android's installer. Android asks you to approve installation; the first time, you may also need to allow this app to request installs. Updates are never silently installed.

Version 1.0.11 adds a 90-second background session grace period while connected. Android may ask for notification permission so the temporary session notification can be shown. Returning to the app stops the service; the service also stops automatically after 90 seconds. Force-stopping the app or losing network connectivity can still end a session.

The app checks for updates on launch and every two minutes; APK releases are also checked when returning to the app. Keep the app open while downloading a full APK. Choose Later to postpone an APK update. Small fixes and full APK releases use stable GitHub hosting.

Manifest signatures and download SHA-256 hashes are checked by the app. Updates are cumulative for their matching base version.
