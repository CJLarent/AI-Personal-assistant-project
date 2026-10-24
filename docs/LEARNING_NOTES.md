# Learning notes

## Checkpoint 1 — permission decisions

Read `core/permissions.py` and run the tests before changing anything.

Questions to explore:
1. Why use `Action` as an `Enum` rather than arbitrary strings?
2. What does `@dataclass(frozen=True)` prevent?
3. Why should the AI model never set `user_approved` itself?

## Your first small exercise

Add a test in `tests/test_permissions.py` proving `RUN_COMMAND` is denied
when no approval is supplied. Do not change the permission implementation
just to make the test pass.

## Later, not implemented yet

- Replace the prototype approval flag with trusted UI confirmation.
- Add tool execution enforcement and audit logging.
- Integrate voice output (Kokoro), then interchangeable model adapters.
