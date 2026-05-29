# Security Policy

## Reporting

Please report security issues privately through GitHub security advisories if
available, or contact the repository owner directly.

## Template Security Expectations

- Generated tools should not accept secrets in command-line flags by default.
- Generated config files are written with mode `0600`.
- HTTP tracing must not print authorization header values.
- Generated examples should avoid destructive API calls unless protected by
  `--dry-run`, confirmation, or explicit command design.
