# Homebrew Publishing

Generated projects include GoReleaser v2 configuration for publishing release
artifacts and Homebrew tap entries.

## Default Tap

The default generated tap is:

```text
jwmoss/homebrew-tap
```

Homebrew's short tap syntax expects the backing GitHub repository to be named
with the `homebrew-` prefix. `brew tap jwmoss/tap` maps to
`https://github.com/jwmoss/homebrew-tap`.

## Required Secret

For cross-repository tap publishing, add this repository secret to the generated
project:

```text
HOMEBREW_TAP_TOKEN
```

The token needs contents write access to the tap repository.

## Release Flow

```bash
git switch main
git pull --ff-only
make release-check
git tag v0.1.0
git push origin v0.1.0
```

Merge changes through a pull request before you tag a release.
The generated release workflow requires reusable CI checks before it runs GoReleaser.
`.goreleaser-version` pins the release tool. GoReleaser builds
multi-platform archives, creates checksums, publishes a GitHub release, and
updates the Homebrew tap.

## Cask vs Formula

The template defaults to `cask` because current GoReleaser v2 validates
`homebrew_casks` without deprecation warnings.

```bash
brew tap jwmoss/tap
brew install --cask jwmoss/tap/mytool
```

Set `homebrew_package_type` to `formula` when generating a project if you need
the older `brew install jwmoss/tap/mytool` formula layout. GoReleaser still
understands that shape, but its check returns exit code 2 for valid deprecated configuration.
Formula-mode checks accept that code only. Invalid configuration still fails.
Use `cask` for new tools.

Set `homebrew_package_type` to `none` to skip tap publication.
GitHub releases remain available and require no tap token.
