# Blocked Worker Runbook

Use this when a worker cannot proceed.

## 1. Classify the block

- missing access
- missing source context
- approval boundary
- validator failure
- dependency failure
- wrong target
- unclear success criteria
- safety boundary

## 2. Check source

Before asking the human, verify what can be checked:

- repo status
- logs
- config
- current public/private visibility
- active ledger entry
- existing approval notes

## 3. Update ledger

```bash
python3 scripts/session_orchestrator.py update \
  --state .orchestrator/state.json \
  --session <id> \
  --status blocked \
  --note "Blocked on <specific ask>"
```

## 4. Post blocked update

```text
Blocked:
- What is blocked:
- Source checked:
- Needed from human:
- Safe fallback:
```

## 5. Continue safe parallel work

If another part is safe and independent, create or update a separate session. Do not let a blocked worker mutate high-risk surfaces while waiting for approval.
