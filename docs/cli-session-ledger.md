# CLI Session Ledger

## Purpose

The ledger is the source of truth for active CLI work. It prevents orphaned sessions, duplicate workers, stale terminals, and unclear ownership.

## Required fields

| Field | Meaning |
|---|---|
| `id` | stable session id |
| `task` | human-readable task |
| `topic` | logical Telegram topic |
| `owner` | orchestrator or worker owner |
| `status` | lifecycle state |
| `created_at` | ISO timestamp |
| `updated_at` | ISO timestamp |
| `target` | repo, host, service, or logical target |
| `risk` | low, medium, high |
| `resume` | resume command or pointer |
| `proof` | validator or source proof |
| `handoff` | latest handoff note |

## JSON shape

```json
{
  "version": 1,
  "sessions": [
    {
      "id": "sess_20260706_120000_ops",
      "task": "Investigate failing tests",
      "topic": "engineering",
      "owner": "orchestrator",
      "status": "active",
      "created_at": "2026-07-06T12:00:00Z",
      "updated_at": "2026-07-06T12:05:00Z",
      "target": "repo:example",
      "risk": "medium",
      "resume": "droid --resume <session-id>",
      "proof": [],
      "handoff": "Checking validator failures."
    }
  ]
}
```

## Ledger operations

- `init`: create empty state
- `create`: register a new session
- `list`: show active work
- `show`: inspect one session
- `update`: add status, note, proof, or handoff
- `close`: mark verified or closed with proof
- `archive`: hide completed sessions from default views

## Staleness policy

Do not use CPU alone to decide whether a session is stuck. Prefer transcript or ledger update time. A session is stale when:

- no ledger update exists past the expected cadence
- no transcript or log has changed recently
- the worker has not reported proof or blocker
- the owner cannot explain next action

## Ownership policy

Only one owner may be accountable for closeout. Multiple workers can contribute, but the ledger must name the owner that verifies and reports the final result.
