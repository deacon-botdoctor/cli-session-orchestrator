# Session State Machine

The ledger state machine is intentionally simple. The point is not bureaucracy, it is preventing hidden work.

## States

| State | Meaning | Required evidence |
|---|---|---|
| `triaged` | request understood | request, topic, risk |
| `assigned` | owner/worker chosen | owner, target, definition of done |
| `active` | work is ongoing | latest note or transcript pointer |
| `blocked` | cannot proceed safely | source checked, blocker, needed input |
| `needs_review` | output exists but is not accepted | artifact or diff pointer |
| `verified` | required proof exists | validator or source evidence |
| `closed` | no further action expected | closeout packet |
| `archived` | hidden from default active view | archival reason |

## Allowed transitions

```text
triaged -> assigned
assigned -> active
active -> blocked
active -> needs_review
active -> verified
blocked -> active
blocked -> closed
needs_review -> active
needs_review -> verified
verified -> closed
closed -> archived
```

Avoid jumping directly from `triaged` to `closed` unless the orchestrator answered directly and recorded why no worker was needed.

## Transition requirements

### To `assigned`

- one accountable owner
- one primary topic
- target or reason target is unknown
- definition of done

### To `active`

- worker/session label
- start note posted to topic
- expected proof named

### To `blocked`

- exact blocker
- source checked
- human input or approval needed
- safe fallback if any

### To `needs_review`

- artifact, diff, branch, or output pointer
- reviewer or approver
- decision needed

### To `verified`

- proof attached
- skipped checks named if any
- remaining risk stated

### To `closed`

- closeout posted or saved
- next action is none or assigned elsewhere
- resume pointer included if future work may continue

## Stale-state rules

A session is suspicious when:

- `triaged` for too long without assignment
- `active` without an update past cadence
- `blocked` without a named human ask
- `needs_review` without a reviewer
- `verified` but not closed after topic update

The orchestrator should report stale sessions, not kill them automatically.
