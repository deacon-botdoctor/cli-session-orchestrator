# Orchestrator Architecture

## Purpose

The orchestrator is the traffic controller for CLI agent work. It turns Telegram topic requests into tracked CLI sessions, routes work to the right worker, and reports progress in a way a human can scan.

## Responsibilities

- classify incoming requests by topic, lane, scope, and risk
- decide whether to answer, spawn work, resume work, or ask for approval
- create a session ledger entry
- assign a worker or tool path
- keep status visible in the correct topic
- preserve handoffs and resume commands
- enforce verification before closeout
- avoid cross-topic and cross-customer bleed

## Non-responsibilities

- storing secrets
- replacing the worker assigned to the task
- silently changing provider, auth, billing, or deployment state
- posting to unrelated topics
- using memory as proof of current runtime state

## Components

| Component | Job |
|---|---|
| Topic router | maps request to one clear topic lane |
| Session ledger | records task, owner, status, target, proof, and resume data |
| Worker dispatcher | launches or assigns CLI agents |
| Progress reporter | emits concise Telegram status updates |
| Handoff writer | creates resume-safe packets |
| Verification gate | blocks vague completion claims |
| Safety gate | blocks destructive, public, credential, billing, and customer-visible mistakes |

## Session lifecycle

```text
requested -> triaged -> assigned -> active -> blocked|needs_review|verified -> closed|archived
```

## Decision loop

1. Read the topic and local context.
2. Check the source of truth for current state if one exists.
3. Classify the request.
4. Choose the smallest competent worker or direct action.
5. Create or update the session ledger.
6. Report the plan in the topic.
7. Execute through the worker.
8. Verify the claim.
9. Post the closeout packet.
10. Persist a sanitized handoff if work can resume later.

## Status vocabulary

- `triaged`: request understood, not yet assigned
- `assigned`: worker or session chosen
- `active`: work is ongoing
- `blocked`: needs user input, approval, credentials, or missing access
- `needs_review`: output exists but requires review
- `verified`: proof exists
- `closed`: no further action
- `archived`: preserved for history

## Core invariant

One task should have one visible owner, one session ledger entry, and one primary Telegram topic. Side work must be explicitly linked, not silently scattered.
