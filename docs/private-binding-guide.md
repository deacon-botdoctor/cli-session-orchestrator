# Private Binding Guide

The public repo should stay generic. A real install needs a private binding layer that connects logical names to real destinations and commands.

## What belongs in private binding

- real Telegram chat IDs
- real Telegram thread IDs
- hostnames and SSH aliases
- local runtime paths
- session transcript paths
- model/provider routing
- customer/account mappings
- approval owners
- deployment commands
- credential and secret-manager references

## What stays public

- logical topic names
- session state machine
- message templates
- CLI command shape
- safety gates
- public-safe examples

## Recommended private files

```text
.orchestrator/private-config.yaml
.orchestrator/topic-bindings.yaml
.orchestrator/worker-bindings.yaml
.orchestrator/state.json
```

Keep `.orchestrator/` ignored by git unless you are building a private internal repo.

## Binding checklist

- [ ] Every logical topic has one real destination.
- [ ] Every approval class has a human owner.
- [ ] Every worker type has a launch or resume path.
- [ ] Every high-risk action names the approval topic.
- [ ] Ledger file is backed up or persisted.
- [ ] Public-safe examples do not contain real IDs.

## Example private binding shape

```yaml
topics:
  engineering:
    chat_id: "<private>"
    thread_id: "<private>"
  approvals:
    chat_id: "<private>"
    thread_id: "<private>"

workers:
  coding:
    launch: "<private command>"
    transcript_glob: "<private path>"
```

Do not commit filled bindings to a public repository.
