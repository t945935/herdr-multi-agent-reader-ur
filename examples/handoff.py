"""باب 6: Agent کے زبانی دعوے کے بجائے واضح handoff record کی توثیق کریں۔"""

import argparse
import hashlib
import json
from pathlib import Path


def validate(record, root):
    required = {"task_id", "from", "to", "completed", "next", "artifacts"}
    if not isinstance(record, dict) or not required <= record.keys():
        raise ValueError("handoff کی ضروری fields غائب ہیں")
    if any(not isinstance(record[key], str) or not record[key].strip()
           for key in ["task_id", "from", "to", "completed", "next"]):
        raise ValueError("handoff کے متنی fields خالی نہیں ہو سکتے")
    if not isinstance(record["artifacts"], list) or not record["artifacts"]:
        raise ValueError("handoff کے لیے artifacts درکار ہیں")
    root = Path(root).resolve()
    for artifact in record["artifacts"]:
        if not isinstance(artifact, dict) or set(artifact) != {"path", "sha256"}:
            raise ValueError("ہر artifact میں path اور sha256 درکار ہیں")
        path = (root / artifact["path"]).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            raise ValueError("artifact path project کے اندر موجود file ہونا چاہیے")
        if hashlib.sha256(path.read_bytes()).hexdigest() != artifact["sha256"]:
            raise ValueError("artifact hash مطابقت نہیں رکھتا")
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("record", type=Path)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    validate(json.loads(args.record.read_text()), args.root)
    print("handoff قبول ہوا")
