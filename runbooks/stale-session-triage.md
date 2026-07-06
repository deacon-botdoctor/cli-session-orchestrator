# Stale Session Triage Runbook

Use this when a session has not updated within its expected cadence.

## 1. Confirm staleness

```bash
python3 scripts/session_orchestrator.py stale --state .orchestrator/state.json --minutes 60
```

Do not use CPU usage as the deciding signal.

## 2. Inspect ledger

```bash
python3 scripts/session_orchestrator.py show --state .orchestrator/state.json --session <id>
```

Look for:

- owner
- target
- resume pointer
- latest handoff
- proof
- blocker

## 3. Check private liveness source

Use the private binding to inspect the worker transcript, log, or session output.

Classify:

- active but quiet
- blocked but not reported
- finished but not closed
- failed without handoff
- unknown

## 4. Post topic update

If still active:

```text
Progress:
- Status: active
- Evidence: transcript updated recently
- Next: waiting for validator output
- Blocker: none
```

If blocked:

```text
Blocked:
- What is blocked:
- Source checked:
- Needed from human:
- Safe fallback:
```

## 5. Close or resume

Only close with proof. If resuming, update the ledger with the resume pointer and next action.
