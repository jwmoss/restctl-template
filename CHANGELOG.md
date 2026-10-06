# Changelog

## Unreleased

- Return JSON `null` for empty successful raw responses, including HTTP 204.

- Restrict credentials and redirects to the intended origin; redact errors and bound response sizes.
- Replace config files safely and block local config writes during dry-run.
- Correct JSON output, numeric precision, usage exits, config paths, and version metadata.
- Add compiled-binary regressions and checks for every Homebrew option.
- Pin Actions and GoReleaser; gate releases on supported-platform and quality checks.
- Preserve GitHub releases when Homebrew publication is disabled.
- Add Claude instruction pointers and a downstream migration report.
- Update Go and Cobra to the verified stable releases.
- Keep legacy formula support with an explicit deprecation-only check allowance.
