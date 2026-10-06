# {{ cookiecutter.project_slug }}

[![CI](https://github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.github_repo }}/actions/workflows/ci.yml/badge.svg)](https://github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.github_repo }}/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/{{ cookiecutter.github_owner }}/{{ cookiecutter.github_repo }})](https://github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.github_repo }}/releases/latest)
[![License: {{ cookiecutter.license }}](https://img.shields.io/badge/License-{{ cookiecutter.license | replace('-', '--') }}-blue.svg)](LICENSE)

{{ cookiecutter.project_description }}.

## Install

### Go

```bash
go install {{ cookiecutter.module_path }}/cmd/{{ cookiecutter.binary_name }}@latest
```

{% if cookiecutter.homebrew_package_type == "formula" %}
### Homebrew

```bash
brew tap {{ cookiecutter.homebrew_tap_owner }}/tap
brew install {{ cookiecutter.homebrew_tap_owner }}/tap/{{ cookiecutter.binary_name }}
```
{% elif cookiecutter.homebrew_package_type == "cask" %}
### Homebrew

```bash
brew tap {{ cookiecutter.homebrew_tap_owner }}/tap
brew install --cask {{ cookiecutter.homebrew_tap_owner }}/tap/{{ cookiecutter.binary_name }}
```
{% endif %}

### Source

```bash
git clone https://github.com/{{ cookiecutter.github_owner }}/{{ cookiecutter.github_repo }}.git
cd {{ cookiecutter.github_repo }}
make build
./bin/{{ cookiecutter.binary_name }} version
```

## Configuration

Initialize a config file:

```bash
{{ cookiecutter.binary_name }} config init --base-url {{ cookiecutter.api_base_url }}
```

The default path uses the operating system config directory:

- Linux: `$XDG_CONFIG_HOME/{{ cookiecutter.binary_name }}/{{ cookiecutter.config_filename }}`, or `~/.config` when unset.
- macOS: `~/Library/Application Support/{{ cookiecutter.binary_name }}/{{ cookiecutter.config_filename }}`.
- Windows: `%AppData%\\{{ cookiecutter.binary_name }}\\{{ cookiecutter.config_filename }}`.

Use `--config` to select another path. `config show` reports the selected path.

Environment variables:

| Variable | Purpose |
| --- | --- |
| `{{ cookiecutter.env_prefix }}_BASE_URL` | API base URL |
| `{{ cookiecutter.env_prefix }}_TOKEN` | API token |
| `{{ cookiecutter.env_prefix }}_AUTH_HEADER` | Auth header name |
| `{{ cookiecutter.env_prefix }}_AUTH_SCHEME` | Auth scheme, for example `Bearer` |

Precedence:

```text
flags > environment > config file > defaults
```

Use environment variables, private config files, or stdin for tokens.
Config writes replace complete files and reject destination symlinks.
New config files use mode `0600` on POSIX systems; Windows uses inherited directory permissions.

The HTTP client sends credentials only to the configured origin.
It rejects cross-origin redirects and buffers at most 64 MiB per response.
Provider code must stream larger downloads.
`raw --json` preserves numeric values and returns `null` for empty successful responses.
It rejects other non-JSON response bodies.

## Usage

```bash
{{ cookiecutter.binary_name }} --help
{{ cookiecutter.binary_name }} --version
{{ cookiecutter.binary_name }} version
{{ cookiecutter.binary_name }} doctor
{{ cookiecutter.binary_name }} {{ cookiecutter.resource_name_plural }} list
{{ cookiecutter.binary_name }} {{ cookiecutter.resource_name_plural }} get 123
{{ cookiecutter.binary_name }} raw GET /v1/me --json
printf '%s\n' "$TOKEN" | {{ cookiecutter.binary_name }} config init --token-stdin --force
{{ cookiecutter.binary_name }} completion zsh > ~/.zfunc/_{{ cookiecutter.binary_name }}
```

## Global Flags

| Flag | Description |
| --- | --- |
| `--config` | Config file path |
| `--base-url` | API base URL override |
| `--version` | Print version information |
| `--json` | Emit JSON to stdout |
| `--plain` | Emit stable plain text where available |
| `--quiet`, `-q` | Suppress non-essential output |
| `--no-color` | Disable color |
| `--timeout` | HTTP timeout |
| `--trace-http` | Log HTTP method/path/status to stderr |
| `--dry-run` | Refuse non-GET HTTP requests and local config writes |
| `--no-input` | Disable interactive prompts |

## Exit Codes

| Code | Meaning |
| --- | --- |
| 0 | Success |
| 1 | Runtime error |
| 2 | Invalid usage |

## Development

```bash
make check
```

Checks do not change source files. Use `make fmt` or `make tidy` to apply changes.
`go test ./...` includes compiled-binary flow tests with isolated config paths and local HTTP fixtures.
Tests use synthetic credentials and require no production access.

## Release

Tag a semver release:

```bash
git switch main
git pull --ff-only
make release-check
git tag v0.1.0
git push origin v0.1.0
```

Merge changes through a pull request before you tag a release.
The release workflow requires Linux, macOS, Windows, and quality checks before publication.
`.goreleaser-version` pins the release tool. Install that version before you run release targets.
`go install` builds use module metadata for version output.
{% if cookiecutter.homebrew_package_type == "formula" %}
The formula option uses deprecated GoReleaser `brews` support.
`make release-check` permits its deprecation-only exit code 2, but still rejects invalid configuration.
Use `cask` for new tools.
{% endif %}
{% if cookiecutter.homebrew_package_type != "none" -%}
Set `HOMEBREW_TAP_TOKEN` before the first tagged release so GoReleaser can
update `{{ cookiecutter.homebrew_tap_owner }}/{{ cookiecutter.homebrew_tap_repo }}`.
{% endif -%}
