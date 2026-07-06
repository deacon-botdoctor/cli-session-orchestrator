# Verification and Safety

## Verification rule

The orchestrator should not post a completion claim until it has proof.

Proof can be:

- validator output
- source-of-truth lookup
- live runtime inspection
- artifact existence and parse/open check
- successful dry-run and approved apply
- reviewer approval

## Required closeout shape

```text
Verified:
- <check>: <result>

Remaining risk:
- <none or specific residual>

Next action:
- <done or next step>

Loop delta:
- <what should improve next time>
```

## High-risk operations

Escalate before:

- public posting or publication
- customer-visible messaging
- deleting, resetting, cleaning, or overwriting files
- changing credentials or auth paths
- changing billing or paid provider routes
- committing, pushing, deploying, or enabling recurrence
- moving work between topics or hosts without a receipt

## Source-first grounding

For current-state claims, inspect the live source:

- repo state: actual git working tree
- process state: target host/process/log
- public visibility: GitHub or hosting metadata
- topic routing: current routing config
- durable policy: company brain or equivalent source-of-truth doc
- previous session: active context or session ledger

If a source cannot be checked, say what could not be checked and mark the fallback unverified.

## Public artifact safety

Before publishing a repo, doc, report, or prompt:

- scan for secrets
- scan for private hostnames and IPs
- remove real chat IDs and thread IDs
- remove customer names unless approved
- remove raw logs and transcripts
- use logical placeholders in examples

## Destructive operation rule

The orchestrator may prepare a plan for destructive work, but should not execute it without explicit approval and a rollback or backup path.
