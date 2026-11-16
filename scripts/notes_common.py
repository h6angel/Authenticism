"""Dependency-free validation for the schema subset used by this project."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def schema_errors(value, schema, root, path="$"):
    if "$ref" in schema:
        target = root
        for part in schema["$ref"].removeprefix("#/").split("/"):
            target = target[part]
        return schema_errors(value, target, root, path)
    errors = []
    types = {
        "object": lambda v: isinstance(v, dict),
        "array": lambda v: isinstance(v, list),
        "string": lambda v: isinstance(v, str),
        "boolean": lambda v: isinstance(v, bool),
        "null": lambda v: v is None,
    }
    expected = schema.get("type")
    if expected:
        allowed = expected if isinstance(expected, list) else [expected]
        if not any(types[t](value) for t in allowed):
            return [f"{path}: expected {expected}"]
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: value outside enum")
    if isinstance(value, str) and len(value.strip()) < schema.get("minLength", 0):
        errors.append(f"{path}: empty or too short")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{path}: too few items")
        for index, item in enumerate(value):
            errors += schema_errors(item, schema.get("items", {}), root, f"{path}[{index}]")
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{path}.{key}: missing")
        properties = schema.get("properties", {})
        for key, item in value.items():
            if key in properties:
                errors += schema_errors(item, properties[key], root, f"{path}.{key}")
            elif schema.get("additionalProperties") is False:
                errors.append(f"{path}.{key}: unknown field")
    return errors


def validate(notes):
    schema = load_json(ROOT / "schemas/research-notes.schema.json")
    errors = schema_errors(notes, schema, schema)
    if errors:
        return errors
    if notes["schema_version"] == "1.1":
        for group in ("context", "reception"):
            if group not in notes["understanding"]:
                errors.append(f"$.understanding.{group}: missing for v1.1")
        if "essay_plan" not in notes:
            errors.append("$.essay_plan: missing for v1.1")
    sources = notes["sources"]
    source_ids = [s["id"] for s in sources]
    entry_ids = [e["id"] for entries in notes["understanding"].values() for e in entries]
    quote_ids = [q["id"] for q in notes["quotes"]]
    for label, ids in [("source", source_ids), ("entry", entry_ids), ("quote", quote_ids)]:
        if len(ids) != len(set(ids)):
            errors.append(f"duplicate {label} id")
    known = set(source_ids)
    for group, entries in notes["understanding"].items():
        for entry in entries:
            if not entry["source_refs"] and entry["status"] == "supported":
                errors.append(f"{entry['id']}: supported entry needs sources")
            for ref in entry["source_refs"]:
                if ref["source_id"] not in known:
                    errors.append(f"{entry['id']}: unknown source {ref['source_id']}")
    for quote in notes["quotes"]:
        if quote["source_id"] not in known:
            errors.append(f"{quote['id']}: unknown source {quote['source_id']}")
    return errors
