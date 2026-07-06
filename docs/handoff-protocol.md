# Handoff Protocol

## Purpose

A handoff lets another agent or a future session resume without guessing.

## Handoff packet

```text
HANDOFF
- Task:
- Topic:
- Session:
- Owner:
- Target:
- Current status:
- Files or systems touched:
- Source evidence checked:
- Validators run:
- Remaining risk:
- Next action:
- Resume command:
- Do not touch:
```

## Worker assignment packet

```text
ASSIGNMENT
- Goal:
- Context:
- Target:
- Constraints:
- Tools allowed:
- Tools forbidden:
- Definition of done:
- Required proof:
- Expected return format:
```

## Review packet

```text
REVIEW REQUEST
- Artifact:
- Diff or output:
- Claims to verify:
- Risk areas:
- Commands already run:
- Decision needed:
```

## Closeout packet

```text
CLOSEOUT
- Result:
- Proof:
- What changed:
- What did not change:
- Remaining risk:
- Follow-up:
- Ledger status:
```

## Handoff quality bar

A good handoff is:

- specific enough to resume
- short enough to read
- free of secrets
- explicit about unresolved risk
- tied to a ledger session
- posted in the correct topic

## What not to hand off

- raw logs
- full transcripts
- credentials
- unrelated topic context
- private identifiers in public artifacts
- unverified claims presented as facts
