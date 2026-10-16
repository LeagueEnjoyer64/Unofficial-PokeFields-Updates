# Private-view draft: PokeFields Mods Test

This isolated test branch stores the signed Android mod test APK in transport parts.
GitHub Actions reconstructs and verifies it, then uploads it to a **draft** release.
The draft is never published, marked latest, or included in any update channel.
The default branch and production release files are not changed.

The APK installs as a separate app, `app.unofficial.pokefields.modtest`.
The normal Android app is not replaced. Production update checks are disabled.
Upscaled Light is included and enabled. Physical-phone/live-battle validation is pending.

The branch is public if the repository is public; a draft release is visible only to authorized repository users. No passwords, signing keys, ROMs, or credentials are included.
