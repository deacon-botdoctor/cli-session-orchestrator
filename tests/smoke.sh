#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
STATE="$(mktemp -t cli-session-orchestrator.XXXXXX.json)"

python3 "$ROOT/scripts/session_orchestrator.py" init --state "$STATE" --force >/dev/null
sid="$(
  python3 "$ROOT/scripts/session_orchestrator.py" create \
    --state "$STATE" \
    --topic engineering \
    --task "Smoke test session" \
    --owner orchestrator \
    --risk low \
    --worker coding \
    --note "Created by smoke test"
)"

python3 "$ROOT/scripts/session_orchestrator.py" update \
  --state "$STATE" \
  --session "$sid" \
  --status active \
  --proof "update worked" >/dev/null

python3 "$ROOT/scripts/session_orchestrator.py" topic-update --state "$STATE" --session "$sid" --kind progress | grep -q "Progress:"
python3 "$ROOT/scripts/session_orchestrator.py" digest --state "$STATE" | grep -q "$sid"
python3 "$ROOT/scripts/session_orchestrator.py" stale --state "$STATE" --minutes 0 | grep -q "$sid"
python3 "$ROOT/scripts/session_orchestrator.py" validate --state "$STATE" | grep -q "ledger_valid=true"
python3 "$ROOT/scripts/session_orchestrator.py" close --state "$STATE" --session "$sid" --proof "close worked" >/dev/null
python3 "$ROOT/scripts/session_orchestrator.py" validate --state "$STATE" | grep -q "ledger_valid=true"
python3 "$ROOT/scripts/session_orchestrator.py" config-check --config "$ROOT/config/orchestrator.example.yaml" | grep -q "config_shape_valid=true"

rm -f "$STATE"
echo "smoke=pass"
