# Ecosystem Direction

`restctl-template` starts as a project generator, but the intended long-term
shape is a small ecosystem of consistent REST API CLIs.

## Near Term

- Keep generated CLIs structurally consistent.
- Publish generated tools through `jwmoss/homebrew-tap`.
- Use shared command contracts so `tool doctor`, `tool config`, `tool raw`,
  `tool --json`, and `tool --plain` behave predictably across projects.
- Keep the template self-test strict enough to prevent broken generated repos.

## Later

- Add a catalog page listing generated tools, install commands, API coverage,
  and maturity.
- Add a shared docs site if several generated tools exist.
- Add reusable design guidance for auth flows, destructive operations, and
  endpoint coverage tiers.
- Add examples generated from real public APIs.

## Candidate Tools

- `unraidctl`: public-ish API wrapper patterns, GraphQL-flavored rather than
  pure REST.
- `skycli`: broad private-API wrapper patterns, useful for safety and command
  coverage lessons.
- Future public REST API tools generated from this template.
