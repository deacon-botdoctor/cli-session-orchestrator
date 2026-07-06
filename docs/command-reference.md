# Command Reference

The reference CLI is intentionally small. It is a ledger and reporting helper, not a full Telegram bot.

## Initialize

```bash
python3 scripts/session_orchestrator.py init --state .orchestrator/state.json
```

Use `--force` only for disposable local tests.

## Create a session

```bash
python3 scripts/session_orchestrator.py create \
  --state .orchestrator/state.json \
  --topic engineering \
  --task "Fix failing tests" \
  --owner orchestrator \
  --target "repo:example" \
  --risk medium \
  --worker coding \
  --resume "droid --resume <id>" \
  --note "Inspect tests, patch minimally, run validators"
```

## List sessions

```bash
python3 scripts/session_orchestrator.py list --state .orchestrator/state.json
python3 scripts/session_orchestrator.py list --state .orchestrator/state.json --all
```

Closed and archived sessions are hidden unless `--all` is passed.

## Show one session

```bash
python3 scripts/session_orchestrator.py show --state .orchestrator/state.json --session <id>
```

## Update status

```bash
python3 scripts/session_orchestrator.py update \
  --state .orchestrator/state.json \
  --session <id> \
  --status active \
  --note "Running scoped tests" \
  --proof "pytest tests/foo passed"
```

## Close

```bash
python3 scripts/session_orchestrator.py close \
  --state .orchestrator/state.json \
  --session <id> \
  --verdict verified \
  --proof "validators passed"
```

## Generate topic update

```bash
python3 scripts/session_orchestrator.py topic-update \
  --state .orchestrator/state.json \
  --session <id> \
  --kind progress
```

Kinds:

- `triage`
- `started`
- `progress`
- `blocked`
- `closeout`

## Find stale sessions

```bash
python3 scripts/session_orchestrator.py stale --state .orchestrator/state.json --minutes 60
```

This reports stale sessions. It does not kill anything.

## Summary

```bash
python3 scripts/session_orchestrator.py summary --state .orchestrator/state.json
```

Use this for an operator-facing topic digest.

## Digest

```bash
python3 scripts/session_orchestrator.py digest --state .orchestrator/state.json
```

Use this when posting a fuller active-session summary to an operator topic.

## Validate ledger

```bash
python3 scripts/session_orchestrator.py validate --state .orchestrator/state.json
```

Validation checks:

- state version
- required session fields
- duplicate session IDs
- valid status and risk values
- timestamp parseability
- proof on verified or closed sessions

## Archive closed sessions

```bash
python3 scripts/session_orchestrator.py archive-closed --state .orchestrator/state.json --days 14
```

This marks old closed sessions as `archived`. It does not delete ledger history.

## Check config shape

```bash
python3 scripts/session_orchestrator.py config-check --config config/orchestrator.example.yaml
```

The public reference check verifies the expected top-level sections. A private deployment can replace this with full schema validation.

## Test

```bash
tests/smoke.sh
```

The smoke test covers init, create, update, topic update, digest, stale, validate, close, and config check.
