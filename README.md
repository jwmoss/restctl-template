# restctl-template

Cookiecutter template for Go CLI tools that wrap REST APIs.

`restctl-template` is a starter kit for quickly spinning up repeatable,
scriptable, release-ready command-line clients for REST APIs. It provides a
ready-to-customize repository skeleton with command structure, client plumbing,
configuration, tests, automation, and publishing defaults already wired in.

The generated project includes:

- Cobra command structure with `config`, `doctor`, `raw`, example resource,
  `completion`, `version`, and root `--version` support.
- A small internal REST client with auth headers, request timeouts, JSON helpers,
  dry-run blocking for mutating calls, API error wrapping, and optional HTTP
  tracing.
- Config loading from flags, environment variables, and a YAML config file.
- Human, JSON, and plain output helpers.
- Go tests for the client, config loader, output formatter, and CLI command
  wiring.
- GitHub Actions CI, Dependabot, issue templates, pull request template,
  CODEOWNERS, AGENTS.md, SECURITY.md, CHANGELOG.md, and MIT license scaffolding.
- GoReleaser v2 release config with Homebrew tap publishing support.

## Usage

Install `uv` if needed:

```bash
brew install uv
```

Generate a project:

```bash
uvx cookiecutter gh:jwmoss/restctl-template
```

For local development against this checkout:

```bash
uvx cookiecutter --no-input -o /tmp .
cd /tmp/acme-api-cli
make check
```

## Template Inputs

The most important prompts are:

| Prompt | Purpose |
| --- | --- |
| `project_name` | Human-readable tool name |
| `project_slug` | Repository directory and default GitHub repo name |
| `binary_name` | CLI executable name |
| `module_path` | Go module path |
| `api_name` | API/service name used in docs and help |
| `api_base_url` | Default API base URL |
| `env_prefix` | Environment variable prefix |
| `resource_name_plural` | Example generated resource command |
| `homebrew_package_type` | `cask`, `formula`, or `none` |
| `homebrew_tap_repo` | Tap repository, default `homebrew-tap` |

## Generated Layout

```text
{{cookiecutter.project_slug}}/
  cmd/{{cookiecutter.binary_name}}/main.go
  internal/api/
  internal/cli/
  internal/config/
  internal/output/
  .github/workflows/
  .goreleaser.yaml
  Makefile
  README.md
```

## Development

Run the template self-test:

```bash
make test
```

Render only:

```bash
make render
```

## Homebrew

Generated projects are ready to publish to `jwmoss/homebrew-tap` by default.
Create the tap repo once, add a `HOMEBREW_TAP_TOKEN` secret to generated
projects, then push semver tags such as `v0.1.0`.

See [docs/homebrew.md](docs/homebrew.md) for the generated release contract.
See [docs/ecosystem.md](docs/ecosystem.md) for the longer-term ecosystem shape.

## License

MIT
