#!/usr/bin/env python3
"""پہلے سے شروع idle Agent کو task دیں اور مخصوص receipt کی تصدیق کریں۔"""
import argparse
import json
import os
import subprocess
import uuid
from pathlib import Path


def call(*args, timeout=310):
    done = subprocess.run(["herdr", *args], text=True, capture_output=True, timeout=timeout)
    if done.returncode:
        raise RuntimeError(done.stderr or done.stdout)
    return json.loads(done.stdout)["result"]


def main():
    parser = argparse.ArgumentParser(description="پہلے سے شروع Agent کو task دیں اور مخصوص receipt verify کریں۔")
    parser.add_argument("target", help="Herdr میں چلتے Agent کا نام")
    parser.add_argument("prompt", type=Path, help="Agent کے لیے prompt file")
    parser.add_argument("--output", type=Path, required=True, help="نئی receipt کا path")
    args = parser.parse_args()
    if os.environ.get("HERDR_ENV") != "1":
        raise SystemExit("Herdr کے اندر سے چلائیں")
    agent = call("agent", "get", args.target)["agent"]
    if agent["agent_status"] not in {"idle", "done"}:
        raise SystemExit("task شروع کرنے سے پہلے Agent idle/done ہونا چاہیے")
    path = args.output.resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise SystemExit("نیا receipt path منتخب کریں؛ پچھلے task کا path دوبارہ نہ لیں")
    task_id = uuid.uuid4().hex
    prompt = args.prompt.read_text() + (
        f"\n\nاس task کا task_id={task_id}\ncompletion_path={path}\n"
        'حقیقی کام مکمل کرنے کے بعد JSON لکھیں: {"task_id":"اوپر والی شناخت","status":"completed",'
        '"summary":"مخصوص نتیجہ اور verification","artifacts":["حقیقی artifact path"]}۔ '
        "کام مکمل نہ ہو تو status کو blocked رکھیں اور summary میں وجہ لکھیں۔ دوسرا Agent شروع نہ کریں۔"
    )
    settled = call("agent", "prompt", args.target, prompt, "--wait", "--timeout", "300000")
    state = settled["agent"]["agent_status"]
    if state not in {"idle", "done"} or not path.is_file():
        raise SystemExit("Agent رک گیا مگر قبول شدہ receipt نہیں؛ agent get/read سے جانچیں")
    receipt = json.loads(path.read_text())
    if receipt.get("task_id") != task_id or receipt.get("status") != "completed" or not receipt.get("summary"):
        raise SystemExit("receipt اس task کو قبول نہیں کرتی")
    for artifact in receipt.get("artifacts", []):
        candidate = Path(artifact)
        if not candidate.is_absolute():
            candidate = Path.cwd() / candidate
        if not candidate.is_file():
            raise SystemExit(f"artifact موجود نہیں: {artifact}")
    print(json.dumps(receipt, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
