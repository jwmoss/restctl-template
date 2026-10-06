# AGENTS.md

## Purpose

`{{ cookiecutter.binary_name }}` is a Go CLI wrapper around the
{{ cookiecutter.api_name }} REST API. Keep provider-specific behavior in
commands and typed API packages; keep generic transport, config, and output
helpers small and reusable.

## CLI Rules

- Primary command output goes to stdout.
- Errors, traces, and diagnostics go to stderr.
- Keep `--json` stable for scripts.
- Keep `--plain` stable and line-oriented where implemented.
- Do not print token values.
- Do not add token/password command-line flags unless there is a documented
  reason and a safer path is still available.
- Guard network mutations and local config or credential writes with `--dry-run`.
- Pass timeout, trace, and safety options to every provider transport.
- Keep raw JSON numbers exact. Use `json.RawMessage` instead of `any` for pass-through payloads.
- Commands that need credentials should explain the missing env/config value in
  the error.

## Validation

Run before handoff:

```bash
make check
```

For release config changes, use the pinned release tool:

```bash
make release-check
```

Keep CLI flow tests at the subprocess boundary in `tests/`.
Use local HTTP fixtures and synthetic credentials.
