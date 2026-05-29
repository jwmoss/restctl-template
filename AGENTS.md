# AGENTS.md

## Purpose

`restctl-template` is a Cookiecutter template for Go command-line tools that
wrap REST APIs. Keep the template focused on repeatable REST CLI infrastructure:
configuration, auth wiring, API client patterns, output contracts, release
automation, and repository metadata.

It is not a place for one provider's private API behavior. Put generated-example
code in the template only when it is reusable across ordinary REST APIs.

## Development Rules

- Preserve the generated project as a real, buildable Go module.
- Keep generated commands script-friendly: primary data goes to stdout; errors,
  traces, and diagnostics go to stderr.
- Keep `--json`, `--plain`, `--quiet`, `--no-color`, `--timeout`, `--trace-http`,
  and `--dry-run` working consistently.
- Do not add token or password flags by default. Prefer env vars, config files
  with mode `0600`, stdin prompts, or future OS keychain integrations.
- Avoid generated app-specific assumptions. The default resource command is an
  example, not a framework boundary.
- When changing template variables, update `cookiecutter.json`, hooks, README,
  docs, and the generated README together.
- If `.goreleaser.yaml` changes, verify that Cookiecutter does not consume
  GoReleaser's `{{ .Version }}` style templates.

## Validation

Run before handoff:

```bash
make test
```

For a generated project, run:

```bash
uvx cookiecutter --no-input -o /tmp .
cd /tmp/acme-api-cli
make check
```

If GoReleaser is installed, also run:

```bash
goreleaser check
```

## Release Model

This template repo itself is released by Git tags. Generated projects own their
own release automation and Homebrew tap publishing through their generated
`.goreleaser.yaml` and `.github/workflows/release.yml`.
