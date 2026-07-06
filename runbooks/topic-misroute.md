# Topic Misroute Runbook

Use this when work appears in the wrong Telegram topic or crosses a lane boundary.

## 1. Stop widening the current topic

Do not keep discussing the work in the wrong topic just because it started there.

## 2. Identify correct lane

Check:

- request type
- customer/account scope
- whether approval is needed
- whether the output is public or customer-visible
- whether this is a report, draft, troubleshooting, or engineering lane

## 3. Post movement receipt

```text
Moved:
- From:
- To:
- Session:
- Reason:
- State synced:
- Resume pointer:
```

## 4. Update ledger

```bash
python3 scripts/session_orchestrator.py update \
  --state .orchestrator/state.json \
  --session <id> \
  --note "Moved from <old-topic> to <new-topic>; reason: <reason>"
```

If the primary topic changes, update the ledger record in the private implementation or create a replacement session and close the old one with a pointer.

## 5. Verify no cross-context leak

Before continuing, ensure the wrong topic did not receive:

- customer-private details
- personal details in a business lane
- approval-only content in a reporting lane
- raw logs or secrets

If it did, escalate to the operator.
