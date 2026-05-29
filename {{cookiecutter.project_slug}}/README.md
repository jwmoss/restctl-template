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

Config path:

```text
$XDG_CONFIG_HOME/{{ cookiecutter.binary_name }}/{{ cookiecutter.config_filename }}
```

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

Tokens are intentionally not accepted as command-line flags by default. Use the
environment, a `0600` config file, or stdin-backed setup.

## Usage

```bash
{{ cookiecutter.binary_name }} --help
{{ cookiecutter.binary_name }} version
{{ cookiecutter.binary_name }} doctor
{{ cookiecutter.binary_name }} {{ cookiecutter.resource_name_plural }} list
{{ cookiecutter.binary_name }} {{ cookiecutter.resource_name_plural }} get 123
{{ cookiecutter.binary_name }} raw GET /v1/me --json
```

## Global Flags

| Flag | Description |
| --- | --- |
| `--config` | Config file path |
| `--base-url` | API base URL override |
| `--json` | Emit JSON to stdout |
| `--plain` | Emit stable plain text where available |
| `--quiet`, `-q` | Suppress non-essential output |
| `--no-color` | Disable color |
| `--timeout` | HTTP timeout |
| `--trace-http` | Log HTTP method/path/status to stderr |
| `--dry-run` | Refuse non-GET HTTP requests |
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

## Release

Tag a semver release:

```bash
git tag v0.1.0
git push origin main
git push origin v0.1.0
```

The release workflow uses GoReleaser to publish archives and checksums.
{% if cookiecutter.homebrew_package_type != "none" -%}
Set `HOMEBREW_TAP_TOKEN` before the first tagged release so GoReleaser can
update `{{ cookiecutter.homebrew_tap_owner }}/{{ cookiecutter.homebrew_tap_repo }}`.
{% endif -%}
