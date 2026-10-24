# Security roadmap — planning document

This repository is public, but the assistant is designed for personal use.
Security controls below are planned, not implemented or verified.

## Access boundaries

- GitHub access: scope external integrations to this repository alone.
- Local files: start with no access; use explicit directories and least privilege.
- Commands and network: disabled until separately designed and tested.
- User approval: must originate from trusted application UI, not model output.

## Future learning milestones

1. Define an allowlist of supported tools and their permissions.
2. Add a trusted approval workflow with one-time authorization.
3. Add tests that demonstrate rejected unauthorized actions.
4. Isolate tool execution using operating-system controls.
5. Add secure credential handling and secret scanning before publishing.
6. Review dependencies and third-party model licenses.

## TODO for the developer

Describe one threat scenario in which a webpage attempts to persuade the
assistant to run a command. Identify which component should reject it and why.
