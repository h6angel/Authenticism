"""Validate notes structure and source references; no literary judgment."""
import argparse
import json
from notes_common import load_json, validate


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("notes")
    args = parser.parse_args()
    try:
        errors = validate(load_json(args.notes))
    except (OSError, ValueError) as exc:
        errors = [str(exc)]
    print(json.dumps({"status": "error" if errors else "passed", "errors": errors}, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
