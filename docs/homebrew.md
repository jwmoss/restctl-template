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
git tag v0.1.0
git push origin main
git push origin v0.1.0
```

The generated release workflow runs GoReleaser on tags. GoReleaser builds
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
understands that shape, but reports it as deprecated in current v2 releases.
