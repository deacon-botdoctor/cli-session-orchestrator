# Observability

The orchestrator needs enough visibility to answer "what is happening?" without reading every transcript.

## Signals

| Signal | Source | Use |
|---|---|---|
| Ledger status | state file | active work inventory |
| Last update time | ledger | stale detection |
| Proof list | ledger | closeout readiness |
| Topic digest | CLI digest | operator status |
| Worker transcript | private binding | liveness evidence |
| Validator output | worker result | verification |
| Approval record | topic or ledger note | audit trail |

## Dashboards

A minimal topic digest should show:

- active sessions
- blocked sessions
- stale sessions
- sessions waiting for review
- verified sessions not closed

Use:

```bash
python3 scripts/session_orchestrator.py summary --state .orchestrator/state.json
python3 scripts/session_orchestrator.py digest --state .orchestrator/state.json
python3 scripts/session_orchestrator.py stale --state .orchestrator/state.json --minutes 60
```

## Alert rules

Alert when:

- a high-risk session is active without an approval note
- a session is stale
- a blocked session does not name the needed human action
- a closed session has no proof
- two sessions appear to own the same target
- work moved topics without a movement receipt

## Human-readable status

Good status:

```text
Session digest:
- sess_... [active] engineering: Fix failing tests
  - Owner: coding
  - Risk: medium
  - Proof: no proof yet
  - Next: running scoped tests
```

Bad status:

```text
2 python processes, 40 percent CPU
```

CPU and process age are weak liveness signals. Prefer ledger and transcript update time.
