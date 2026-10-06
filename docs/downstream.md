# Downstream consistency and migration

Source snapshot: 2026-10-06. This report compares five public CLI repositories.
Template changes affect new projects only. Existing repositories require separate changes.

## Shared fixes in this update

| Contract | Reference fixes |
| --- | --- |
| Restrict credentials and redirects; redact errors | [Skycli efacbb5](https://github.com/jwmoss/skycli/commit/efacbb51f76d9c96b1d9995b22b9a5d36639cdd6), [Unraidctl dd873b8](https://github.com/jwmoss/unraidctl/commit/dd873b8ec54462f61e9557320130f39a32937e46) |
| Private config replacement and exact JSON numbers | [ClassReach 2563d03](https://github.com/jwmoss/classreach/commit/2563d03c5b5918a8c1b9738e2a81a829e7dfa0f9) |
| Dry-run guards for config and credential writes | [EDC fbeed3a](https://github.com/jwmoss/edcctl/commit/fbeed3abb6f0832315eb10cb370710b4f3e3d128), [Goveetl 2177281](https://github.com/jwmoss/goveetl/commit/2177281cb3803c6b7173a21ab8f5f91e4c7751df) |
| CI security and supported-platform release gates | [Skycli 5e672e3](https://github.com/jwmoss/skycli/commit/5e672e38e8d3cfd166cdc4b64ba74d9a86a6262f), [ClassReach 2563d03](https://github.com/jwmoss/classreach/commit/2563d03c5b5918a8c1b9738e2a81a829e7dfa0f9) |
| Compiled-binary flow coverage | [ClassReach 4252a00](https://github.com/jwmoss/classreach/commit/4252a00b19625fd5d26adadb51e6a335d5a8bebe), [EDC fbeed3a](https://github.com/jwmoss/edcctl/commit/fbeed3abb6f0832315eb10cb370710b4f3e3d128) |
| Version metadata for module installs | [Skycli 1a3476b](https://github.com/jwmoss/skycli/commit/1a3476b0abb0998e06886a8628f2b8cc272b520a) |

The template also repairs local flag validation, usage exits, selected config paths, and JSON config initialization.
Its tests verify these behaviors through the compiled executable.
The transport tests separately cover response limits and custom HTTP client policies.

## Existing repositories: recommended next changes

### Goveetl — highest priority

Audited commit: [97ac998](https://github.com/jwmoss/goveetl/tree/97ac998).

- Apply the HTTP credential, redirect, and error-redaction fixes to `internal/api/client.go`.
- Replace direct config writes in `internal/config/config.go` with private, symlink-safe publication.
- Apply the version, usage-exit, config-path, and JSON fixes.
- Replace mutable action tags and the unchecked release job with the shared CI baseline.
- Pass global timeout and trace options to app and OpenAPI clients, not only the raw client.
- Add compiled-binary flows for each transport and its safety flags.

The [shared client](https://github.com/jwmoss/goveetl/blob/97ac998/internal/api/client.go) still attaches credentials to absolute URLs.
[Provider constructors](https://github.com/jwmoss/goveetl/blob/97ac998/internal/cli/app_session.go) construct separate clients.
The app and OpenAPI implementations set their own fixed timeouts.
The [release workflow](https://github.com/jwmoss/goveetl/blob/97ac998/.github/workflows/release.yml) still uses mutable action tags and a floating GoReleaser version.

Keep Govee wire formats, app headers, MQTT, and LAN behavior provider-specific.

### EDC — finish config and CLI safety

Audited commit: [fbeed3a](https://github.com/jwmoss/edcctl/tree/fbeed3a).

- Replace chmod-then-write config updates with private-file replacement.
- Fix selected-path output and usage error classification.
- Add module-version fallback for `go install`.
- Require the full platform and flow suite before release publication.

The [config writer](https://github.com/jwmoss/edcctl/blob/fbeed3a/internal/config/config.go) repairs permissions but still follows destination symlinks.
The [config command](https://github.com/jwmoss/edcctl/blob/fbeed3a/internal/cli/config_cmd.go) reports the default path instead of the selected path.
Its release job runs `make check`, but does not reuse the complete CI workflow.
Retain EDC's stricter portal redirect policy and provider-specific login flow.

### Unraidctl — config safety and release consistency

Audited commit: [8198fa1](https://github.com/jwmoss/unraidctl/tree/8198fa1).

- Replace direct config writes with private-file replacement.
- Return config read errors other than file-not-found.
- Use `go-version-file: go.mod` for releases.
- Pin GoReleaser and require the full test workflow before publication.

The [config loader](https://github.com/jwmoss/unraidctl/blob/8198fa1/internal/config/config.go) ignores filesystem read errors.
The same file uses `os.WriteFile`, which preserves permissive modes on existing files.
The [release workflow](https://github.com/jwmoss/unraidctl/blob/8198fa1/.github/workflows/release.yml) selects Go 1.22.x and floating GoReleaser v2 without a test dependency.
Keep its GraphQL schema checks and existing credential-redaction work.

### ClassReach — small consistency fixes

Audited commit: [4252a00](https://github.com/jwmoss/classreach/tree/4252a00).

ClassReach already supplies the strongest config writer and reusable release gates in this comparison.
Add module-version fallback to [version output](https://github.com/jwmoss/classreach/blob/4252a00/internal/cli/root.go).
Keep its tenant validation, response cap, and no-I/O dry-run behavior.

### Skycli — retain its mature safeguards

Audited commit: [d857759](https://github.com/jwmoss/skycli/tree/d857759).

Skycli already has origin checks, version fallback, auth safety guards, refresh locks, and broad flow coverage.
Do not replace those features with the smaller template implementation.
Use it as a reference for provider-auth extensions.

## Deliberate differences

- Dry-run has different semantics today. ClassReach previews without network calls; the template permits reads but blocks mutations and local config writes.
- Config paths differ. The template uses native operating system paths; some tools use XDG-style paths across platforms.
- CLI parsers differ. Preserve each tool's public interface rather than replace it solely for structural similarity.
- Existing suites use a separate E2E runner. The template uses Go subprocess tests to avoid another runtime.
- OAuth, SRP, GraphQL, session locks, device transports, and provider discovery stay outside the generic template.

Choose one documented dry-run contract before a cross-repository behavior change.
Use an explicit migration if config paths must change. Never silently abandon an existing credential file.

## Migration order

1. Apply credential and private-file fixes.
2. Add failing subprocess regressions for each affected command.
3. Repair CLI output and usage behavior.
4. Apply CI and release gates.
5. Add optional agent discovery, environment defaults, or pre-commit hooks only where useful.

The source comparison identifies downstream work; it does not claim those repositories pass the new template tests.
