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
  origin-scoped credentials, redirect restrictions, bounded responses, dry-run
  guards, redacted errors, and optional HTTP traces.
- Config loading from flags, environment variables, and a YAML config file.
- Human, JSON, and plain output helpers.
- Package tests and compiled-binary flow tests with local HTTP fixtures.
- Private config replacement that rejects destination symlinks.
- CI checks on Linux, macOS, and Windows before release publication.
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

Install Go, uv, and the GoReleaser version from
`{{cookiecutter.project_slug}}/.goreleaser-version`.

Run the template self-test:

```bash
make test
```

The self-test checks all three Homebrew options, generated workflows, and CLI behavior.
It uses temporary directories and synthetic credentials.
It never calls a production API.
Formula checks permit GoReleaser exit code 2 for the documented legacy deprecation.

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
See [docs/downstream.md](docs/downstream.md) for shared fixes and remaining differences across existing CLI repositories.

Template changes affect new projects only. Apply the linked fixes to existing tools separately.

## License

MIT
