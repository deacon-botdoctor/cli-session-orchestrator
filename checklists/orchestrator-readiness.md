# Orchestrator Readiness Checklist

## Config

- [ ] Logical topics defined.
- [ ] Private destination bindings exist outside the public repo.
- [ ] Owner for each topic is named.
- [ ] Worker types are defined.
- [ ] Approval topics are defined.
- [ ] Update cadence is defined.

## Ledger

- [ ] Ledger path exists.
- [ ] `init` has been run.
- [ ] New sessions can be created.
- [ ] Status updates can be recorded.
- [ ] Topic updates can be generated.
- [ ] Stale sessions can be listed.
- [ ] Closed sessions are hidden by default.

## Dispatch

- [ ] Direct answer vs resume vs spawn rules are understood.
- [ ] Worker packet template is used.
- [ ] Parallel workers are isolated.
- [ ] Owner is accountable for closeout.

## Telegram

- [ ] Updates use templates.
- [ ] Topic moves include receipts.
- [ ] No raw logs are posted by default.
- [ ] Blocked updates include the human ask.
- [ ] Closeouts include proof.

## Safety

- [ ] Public safety scan exists.
- [ ] Destructive operations require approval.
- [ ] Credential and billing changes require approval.
- [ ] Customer-visible messaging requires approval.
- [ ] Commit/push/deploy gates are separate.

## Verification

- [ ] CLI compiles.
- [ ] CLI smoke test passes.
- [ ] Example YAML parses.
- [ ] Public docs contain no private IDs.
- [ ] Closeout format includes verified, risk, next action, and loop delta.
