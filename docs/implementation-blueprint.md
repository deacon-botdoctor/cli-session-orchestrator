# Implementation Blueprint

This is the practical path for wiring the orchestrator into a real agent.

## Phase 0: Private binding

The public repo uses logical names. A real install needs a private config that maps:

- logical topic names to chat/thread destinations
- allowed worker types
- allowed hosts or execution lanes
- approval topics
- default update cadence
- source-of-truth lookup commands
- validator commands
- session transcript locations

Start from `config/orchestrator.example.yaml`, but keep the filled version private.

## Phase 1: Read-only ledger

Goal: track work without controlling it yet.

Actions:

1. Initialize the ledger.
2. Register new CLI work manually.
3. Update status when work starts, blocks, or verifies.
4. Generate topic updates from ledger state.
5. Run stale-session reports.

Definition of done:

- every active CLI session has a ledger entry
- every ledger entry has one topic and one owner
- stale sessions are visible without inspecting raw processes

## Phase 2: Orchestrated dispatch

Goal: make the orchestrator the front door for new CLI work.

Actions:

1. Classify incoming topic messages.
2. Decide direct answer vs resume vs spawn vs delegate.
3. Create an assignment packet.
4. Record the session before work starts.
5. Post a `Started` update to the topic.

Definition of done:

- no worker starts without a ledger entry
- every assignment includes required proof
- topic updates tell the human where work lives

## Phase 3: Verification-gated closeout

Goal: stop vague completion claims.

Actions:

1. Add proof requirements by work type.
2. Block `closed` status unless proof or explicit skipped-check reason exists.
3. Emit closeout packets with verified, risk, next action, and resume pointer.

Definition of done:

- closeout is impossible without proof or an explicit "not verified" note
- public or customer-visible work goes through safety review
- commit, push, deploy, and destructive actions have separate gates

## Phase 4: Topic-aware automation

Goal: automate the boring parts without hiding side effects.

Safe automations:

- stale session report
- session ledger summary
- missing-proof report
- topic lane violation report
- handoff reminder

Risky automations requiring approval:

- launching workers
- posting externally
- changing repo state
- committing or pushing
- deploying
- modifying credentials, billing, or provider routes

## Phase 5: Durable learning

Goal: improve the operating system.

Actions:

1. Promote recurring failure patterns into checklists.
2. Promote repeatable workflows into skills or runbooks.
3. Keep raw transcripts out of durable docs.
4. Store only sanitized pointers in shared memory.

## Install checklist

- [ ] Private topic map exists.
- [ ] Ledger path exists and is backed up or persisted.
- [ ] Logical topics are mapped to real destinations privately.
- [ ] Worker types are defined.
- [ ] Approval topics are defined.
- [ ] Stale-session cadence is defined.
- [ ] Closeout proof requirements are defined.
- [ ] Handoff format is accepted by the operator.
- [ ] Public safety scan is available before publishing artifacts.
