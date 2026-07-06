#!/usr/bin/env python3
"""Small public-safe reference CLI for a session ledger."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"version": 1, "sessions": []}
    return json.loads(path.read_text())


def save_state(path: Path, state: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")


def session_id(topic: str) -> str:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    safe_topic = "".join(ch if ch.isalnum() else "_" for ch in topic.lower()).strip("_") or "topic"
    return f"sess_{stamp}_{safe_topic}"


def find_session(state: dict[str, Any], sid: str) -> dict[str, Any]:
    for session in state["sessions"]:
        if session["id"] == sid:
            return session
    raise SystemExit(f"session not found: {sid}")


def cmd_init(args: argparse.Namespace) -> None:
    path = Path(args.state)
    if path.exists() and not args.force:
        raise SystemExit(f"state already exists: {path}")
    save_state(path, {"version": 1, "sessions": []})
    print(f"initialized {path}")


def cmd_create(args: argparse.Namespace) -> None:
    path = Path(args.state)
    state = load_state(path)
    created = now()
    sid = session_id(args.topic)
    state["sessions"].append(
        {
            "id": sid,
            "task": args.task,
            "topic": args.topic,
            "owner": args.owner,
            "status": "triaged",
            "created_at": created,
            "updated_at": created,
            "target": args.target or "",
            "risk": args.risk,
            "worker": args.worker or "",
            "resume": args.resume or "",
            "proof": [],
            "handoff": args.note or "",
            "public_safe": True,
            "notes": [args.note] if args.note else [],
        }
    )
    save_state(path, state)
    print(sid)


def cmd_list(args: argparse.Namespace) -> None:
    state = load_state(Path(args.state))
    for session in state["sessions"]:
        if args.all or session["status"] not in {"closed", "archived"}:
            print(f"{session['id']}\t{session['status']}\t{session['topic']}\t{session['task']}")


def cmd_show(args: argparse.Namespace) -> None:
    state = load_state(Path(args.state))
    print(json.dumps(find_session(state, args.session), indent=2, sort_keys=True))


def cmd_update(args: argparse.Namespace) -> None:
    path = Path(args.state)
    state = load_state(path)
    session = find_session(state, args.session)
    if args.status:
        session["status"] = args.status
    if args.note:
        session.setdefault("notes", []).append(args.note)
        session["handoff"] = args.note
    if args.proof:
        session.setdefault("proof", []).append(args.proof)
    if args.resume:
        session["resume"] = args.resume
    session["updated_at"] = now()
    save_state(path, state)
    print(f"updated {args.session}")


def cmd_close(args: argparse.Namespace) -> None:
    path = Path(args.state)
    state = load_state(path)
    session = find_session(state, args.session)
    session["status"] = "closed"
    session["updated_at"] = now()
    session["verdict"] = args.verdict
    if args.proof:
        session.setdefault("proof", []).append(args.proof)
    save_state(path, state)
    print(f"closed {args.session}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage a public-safe CLI session ledger.")
    sub = parser.add_subparsers(required=True)

    init = sub.add_parser("init")
    init.add_argument("--state", required=True)
    init.add_argument("--force", action="store_true")
    init.set_defaults(func=cmd_init)

    create = sub.add_parser("create")
    create.add_argument("--state", required=True)
    create.add_argument("--topic", required=True)
    create.add_argument("--task", required=True)
    create.add_argument("--owner", default="orchestrator")
    create.add_argument("--target")
    create.add_argument("--risk", choices=["low", "medium", "high"], default="medium")
    create.add_argument("--worker")
    create.add_argument("--resume")
    create.add_argument("--note")
    create.set_defaults(func=cmd_create)

    list_cmd = sub.add_parser("list")
    list_cmd.add_argument("--state", required=True)
    list_cmd.add_argument("--all", action="store_true")
    list_cmd.set_defaults(func=cmd_list)

    show = sub.add_parser("show")
    show.add_argument("--state", required=True)
    show.add_argument("--session", required=True)
    show.set_defaults(func=cmd_show)

    update = sub.add_parser("update")
    update.add_argument("--state", required=True)
    update.add_argument("--session", required=True)
    update.add_argument("--status", choices=["triaged", "assigned", "active", "blocked", "needs_review", "verified", "closed", "archived"])
    update.add_argument("--note")
    update.add_argument("--proof")
    update.add_argument("--resume")
    update.set_defaults(func=cmd_update)

    close = sub.add_parser("close")
    close.add_argument("--state", required=True)
    close.add_argument("--session", required=True)
    close.add_argument("--verdict", choices=["verified", "closed", "abandoned"], default="verified")
    close.add_argument("--proof")
    close.set_defaults(func=cmd_close)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
