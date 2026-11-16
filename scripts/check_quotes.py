"""Match verbatim quotes to local source snapshots; never fetch the network."""
import argparse
import json
import re
from pathlib import Path
from notes_common import load_json, validate


def normalize(text):
    # Only line-ending and whitespace normalization; punctuation is significant.
    return re.sub(r"\s+", " ", text).strip()


def check(notes, base):
    sources = {s["id"]: s for s in notes["sources"]}
    results = []
    for quote in notes["quotes"]:
        source = sources[quote["source_id"]]
        result = {"id": quote["id"], "source_id": source["id"]}
        snapshot = source.get("snapshot")
        if quote["kind"] != "verbatim":
            result.update(status="unverifiable", reason="self-translation needs semantic review")
        elif not snapshot:
            result.update(status="unverifiable", reason="no local snapshot")
        else:
            path = (base / snapshot).resolve()
            if not path.is_relative_to(base.resolve()):
                result.update(status="error", reason="snapshot outside task directory")
            else:
                try:
                    text = path.read_text(encoding="utf-8-sig")
                    if quote["text"] in text:
                        result.update(status="matched", mode="exact")
                    elif normalize(quote["text"]) in normalize(text):
                        result.update(status="matched", mode="whitespace")
                    else:
                        result.update(status="mismatch", reason="quote absent from snapshot")
                except (OSError, UnicodeError) as exc:
                    result.update(status="unverifiable", reason=str(exc))
        results.append(result)
    code = 1 if any(r["status"] in {"error", "mismatch"} for r in results) else (
        2 if any(r["status"] == "unverifiable" for r in results) else 0)
    return {"status": "error" if code == 1 else "unverifiable" if code == 2 else "passed",
            "checked": len(results), "results": results,
            "limit": "Text presence only; attribution, location and interpretation require review."}, code


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("notes")
    args = parser.parse_args()
    try:
        path = Path(args.notes).resolve()
        notes = load_json(path)
        errors = validate(notes)
        if errors:
            report, code = {"status": "error", "errors": errors}, 1
        else:
            report, code = check(notes, path.parent)
    except (OSError, ValueError) as exc:
        report, code = {"status": "error", "errors": [str(exc)]}, 1
    print(json.dumps(report, ensure_ascii=False))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
