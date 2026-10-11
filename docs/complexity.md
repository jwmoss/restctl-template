# Complexity checks with cccc

Use [moznion/cccc](https://github.com/moznion/cccc) to measure cognitive and cyclomatic complexity.
Version 1.8.0 is the current release verified on 2026-10-10.
The local `cccc` executable already reports that version.

Cognitive complexity measures how difficult control flow is to follow.
Cyclomatic complexity measures independent control-flow paths.
Neither metric proves correctness or replaces live end-to-end tests.

## Local reports

Run this command from a Go CLI repository:

```bash
cccc --no-config --lang go --exclude '*_test.go' --top-cognitive 10 --table cmd internal
```

Include `pkg` when the repository has that directory.
For Python projects, select `src` or the production `scripts` directory:

```bash
cccc --no-config --lang python --exclude '*_pb2.py' --top-cognitive 10 --table src
```

Analyze a rendered project when you inspect this template.
The unrendered Go files contain Cookiecutter syntax.

## Shared configuration

Add `cccc.toml` to each repository:

```toml
exclude = ["*_test.go", "test_*.py", "*_pb2.py", "tests/**", "test/**", "vendor/**", "node_modules/**"]
```

Use `cccc cmd internal` for Go, or `cccc src` for Python.
Keep reports separate from the build gate until the existing functions meet an agreed limit.
Start with cognitive 15 and cyclomatic 10 as review targets, not automatic refactor requirements.

When a repository meets those limits, add:

```toml
max-cognitive = 15
max-cyclomatic = 10
```

Then `cccc` returns a failure when any selected function exceeds a limit.
The current tool has no native changed-function baseline gate.
Do not describe a whole-file check as a changed-function check.

## GitHub Actions

The [cccc action](https://github.com/moznion/cccc-action) installs a release binary and verifies its SHA-256 checksum.
Add this step to an existing quality job after checkout:

```yaml
- name: Report source complexity
  uses: moznion/cccc-action@f766d74cf323cd9085c2c9263cebdf1ec1ebfb19 # v1.1.1
  with:
    version: v1.8.0
    path: cmd internal
    config: cccc.toml
    top-cognitive: '10'
    args: --table
```

Use `path: src` for Python projects.
Use `path: cmd internal pkg` when all three directories exist.
Retain SHA pins, `persist-credentials: false`, and the repository's workflow lint checks.

## Initial measurements

These measurements exclude Go test files and use production directories.
Each pair shows the largest cognitive and cyclomatic value; the maxima can belong to different functions.

| CLI | Maximum cognitive / cyclomatic |
| --- | --- |
| Forage | 126 / 60 |
| Skycli | 71 / 57 |
| Goveetl | 57 / 45 |
| Brytectl | 35 / 28 |
| Roborocli | 30 / 20 |
| Sleeperctl | 23 / 20 |
| ClassReach | 21 / 15 |
| Edcctl | 21 / 18 |
| Unraidctl | 16 / 12 |

Measure a function before and after a requested change.
Reduce unnecessary branches when that change touches the function.
Keep validation and error handling even when they increase the score.
