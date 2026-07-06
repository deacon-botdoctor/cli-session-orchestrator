# Telegram Topic Coordination

## Goal

Telegram topics should show the human what is happening without forcing them to read raw terminal logs.

## Topic lane rules

- Each topic has one purpose.
- Do not widen a topic contract silently.
- Keep draft/review, reporting, troubleshooting, and approvals separate.
- Customer-specific topics must not receive another customer's context.
- Personal topics must not receive business or customer details.
- If the work moves to another host, session, or topic, say so explicitly.

## Message types

### Triage

```text
Triage:
- Request:
- Topic lane:
- Owner:
- Scope:
- Risk:
- Next action:
```

### Work started

```text
Started:
- Session:
- Worker:
- Target:
- Plan:
- Expected proof:
```

### Progress

```text
Progress:
- Status:
- Evidence:
- Next:
- Blocker:
```

### Blocked

```text
Blocked:
- What is blocked:
- Source checked:
- Needed from human:
- Safe fallback:
```

### Closeout

```text
Closeout:
- Result:
- Verified:
- Remaining risk:
- Next action:
- Resume pointer:
```

## Clarity standard

Good topic update:

> "I assigned this to a CLI session, it is checking the repo tests now, and I will report back here with validator output before calling it complete."

Bad topic update:

> "Working."

## Topic movement receipt

When moving work from one session, host, or topic to another, include:

- source topic
- target topic
- source session id or label
- target session id or label
- whether files/state were synced
- exact resume command or pointer
- why the move happened

## Public examples

Use logical names:

- `ops`
- `engineering`
- `client-alpha`
- `approvals`
- `reports`

Bind those names to real Telegram chat/thread IDs only in private config.
