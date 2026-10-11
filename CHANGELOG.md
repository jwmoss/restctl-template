# Changelog

## Unreleased

## [0.1.0] - 2026-10-10

- Keep live end-to-end tests and static checks; remove unit and fake-server tests.
- Document cccc reports, baseline metrics, and optional complexity limits.
- Return JSON `null` for empty successful raw responses, including HTTP 204.

- Restrict credentials and redirects to the intended origin; redact errors and bound response sizes.
- Replace config files safely and block local config writes during dry-run.
- Correct JSON output, numeric precision, usage exits, config paths, and version metadata.
- Add live compiled-binary checks and static checks for every Homebrew option.
- Pin Actions and GoReleaser; gate releases on supported-platform and quality checks.
- Preserve GitHub releases when Homebrew publication is disabled.
- Add Claude instruction pointers and a downstream migration report.
- Update Go and Cobra to the verified stable releases.
- Keep legacy formula support with an explicit deprecation-only check allowance.
