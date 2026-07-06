# Worker Dispatch

## Dispatch question

For every request, the orchestrator chooses one path:

1. answer directly
2. resume an existing session
3. spawn a new CLI session
4. delegate to a specialist worker
5. ask for approval or missing context

## Decision table

| Request shape | Default action |
|---|---|
| Simple factual answer with source available | answer directly with source checked |
| Existing task continuation | resume existing session |
| Repo/code work | create session, inspect repo, assign coding worker |
| Incident or broken path | create session, classify failure, verify live state |
| Public/client-visible artifact | create session, add output safety gate |
| Destructive or credential-affecting request | ask approval before mutation |
| Ambiguous broad request | ask one scope question or create planning session |

## Worker packet minimum

Every delegated worker should receive:

- goal
- source context
- target path or system
- constraints
- forbidden actions
- proof required
- return format

## Forbidden silent actions

Workers must not silently:

- switch topics
- switch hosts
- change public visibility
- commit or push
- deploy
- delete or clean files
- mutate credentials
- send customer-visible messages
- widen scope beyond the assignment

## Parallel work

Parallel workers are allowed only when their touch surfaces are isolated.

Good split:

- one worker investigates docs
- one worker runs tests
- one worker audits public-safety terms

Bad split:

- two workers edit the same files
- one worker changes config while another validates against old config
- multiple workers post uncoordinated topic updates

## Return format

Workers should return:

```text
Worker result:
- Status:
- Files/systems touched:
- Proof:
- Blockers:
- Risks:
- Recommended next action:
```

The orchestrator then decides what to post publicly in the topic.
