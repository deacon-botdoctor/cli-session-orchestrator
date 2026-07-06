# Escalation Matrix

The orchestrator should know when to keep moving and when to stop for approval.

## Risk classes

| Risk | Examples | Default |
|---|---|---|
| Low | read-only lookup, local notes, status summary | proceed |
| Medium | local file edits, tests, private draft artifacts | proceed with validation |
| High | public output, customer-visible messaging, commit, push, deploy | approval or explicit user instruction |
| Critical | credentials, billing, destructive cleanup, production changes | explicit approval card |

## Approval card

```text
Approval needed:
- Action:
- Why:
- Target:
- Blast radius:
- Rollback:
- Verification:
- Safe alternative:
```

## Escalate before

- publishing a repo or doc publicly
- sending a customer-visible message
- changing repository visibility
- committing unrelated changes
- pushing to a remote
- deploying
- enabling recurrence
- changing model/provider/billing routes
- deleting, resetting, cleaning, or overwriting files
- writing direct database or memory-store changes

## Do not escalate for

- read-only source checks
- local draft creation inside a new repo
- validator runs
- non-destructive status reports
- asking a worker for analysis

## Blocked-state quality bar

When blocked, the orchestrator must say:

- exactly what could not be checked or done
- what was checked
- what decision or access is needed
- what safe fallback exists
- whether work can continue on another part

## No silent downgrade

If the safest path is to stop, stop. Do not silently downgrade by:

- skipping validators
- changing the target
- using stale memory instead of live state
- posting to a different topic
- switching provider or host
- turning a high-risk mutation into a "cleanup"
