# Template Design

`restctl-template` generates a complete Go CLI repository for wrapping REST APIs.

## Boundaries

Generated tools own:

- provider-specific endpoint paths and data types
- authentication flow details
- command names and resource semantics
- destructive operation confirmation rules

The template owns:

- command layout
- config precedence
- common REST client mechanics
- output conventions
- test scaffolding
- release and Homebrew publishing scaffolding
- GitHub metadata

## CLI Contract

The generated CLI follows the Command Line Interface Guidelines baseline:

- Return zero on success and non-zero on failure.
- Send primary output to stdout.
- Send errors, logs, traces, and diagnostics to stderr.
- Show help on `-h` and `--help`.
- Provide machine-readable `--json`.
- Provide stable text where useful through `--plain`.

## REST Wrapper Contract

The generated REST client handles:

- base URL normalization
- auth header injection
- JSON request encoding
- JSON response decoding
- status-code errors with response body snippets
- timeout control
- dry-run refusal for non-GET methods
- optional HTTP tracing without dumping auth headers

## Why Cookiecutter

Cookiecutter keeps the repository repeatable without forcing a custom generator
binary. It also makes CI straightforward: render the default project and run its
normal Go checks.
