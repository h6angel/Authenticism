import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from notes_common import load_json, validate
from check_quotes import check


class ToolsTest(unittest.TestCase):
    def setUp(self):
        self.notes = load_json(ROOT / "evaluations/fixtures/valid-notes.json")
        self.base = ROOT / "evaluations/fixtures"

    def test_valid(self):
        self.assertEqual(validate(self.notes), [])
        report, code = check(self.notes, self.base)
        self.assertEqual(code, 0)
        self.assertEqual(report["results"][0]["mode"], "exact")

    def test_missing_field_wrong_type_and_unknown_field(self):
        for mutation in (lambda n: n.pop("work"), lambda n: n.update(sources="wrong"),
                         lambda n: n.update(unexpected=True)):
            n = copy.deepcopy(self.notes)
            mutation(n)
            self.assertTrue(validate(n))

    def test_dangling_source_and_duplicates(self):
        self.notes["quotes"][0]["source_id"] = "absent"
        self.assertTrue(validate(self.notes))
        self.notes["quotes"][0]["source_id"] = "S1"
        self.notes["sources"].append(copy.deepcopy(self.notes["sources"][0]))
        self.assertTrue(validate(self.notes))

    def test_supported_entry_needs_evidence(self):
        self.notes["understanding"]["story"][0]["source_refs"] = []
        self.assertTrue(validate(self.notes))

    def test_mismatch(self):
        self.notes["quotes"][0]["text"] = "A sentence that was never written."
        self.assertEqual(check(self.notes, self.base)[1], 1)

    def test_whitespace_only(self):
        self.notes["quotes"][0]["text"] = "She brought the letter. He put it under the cup."
        report, code = check(self.notes, self.base)
        self.assertEqual(code, 0)
        self.assertEqual(report["results"][0]["mode"], "whitespace")

    def test_punctuation_not_ignored(self):
        self.notes["quotes"][0]["text"] = "She brought the letter!"
        self.assertEqual(check(self.notes, self.base)[1], 1)

    def test_unverifiable_and_translation(self):
        for snapshot in (None, "missing.txt"):
            n = copy.deepcopy(self.notes)
            if snapshot:
                n["sources"][0]["snapshot"] = snapshot
            else:
                n["sources"][0].pop("snapshot")
            self.assertEqual(check(n, self.base)[1], 2)
        self.notes["quotes"][0]["kind"] = "self_translation"
        self.assertEqual(check(self.notes, self.base)[1], 2)

    def test_path_escape(self):
        self.notes["sources"][0]["snapshot"] = "../outside.txt"
        self.assertEqual(check(self.notes, self.base)[1], 1)

    def test_no_quotes(self):
        self.notes["quotes"] = []
        report, code = check(self.notes, self.base)
        self.assertEqual((code, report["checked"]), (0, 0))

    def test_cli_error_and_unverifiable_exit_codes(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "notes.json"
            self.notes["sources"][0].pop("snapshot")
            path.write_text(json.dumps(self.notes), encoding="utf-8")
            command = [sys.executable, str(ROOT / "scripts/check_quotes.py"), str(path)]
            run = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(run.returncode, 2)
            self.assertEqual(json.loads(run.stdout)["status"], "unverifiable")
            self.notes["quotes"][0]["source_id"] = "unknown"
            path.write_text(json.dumps(self.notes), encoding="utf-8")
            run = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(run.returncode, 1)

    def test_cli_success_and_bad_json(self):
        for script in ("validate_notes.py", "check_quotes.py"):
            command = [sys.executable, str(ROOT / "scripts" / script)]
            run = subprocess.run(command + [str(self.base / "valid-notes.json")], capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertEqual(json.loads(run.stdout)["status"], "passed")
            with tempfile.TemporaryDirectory() as folder:
                bad = Path(folder) / "bad.json"
                bad.write_text("{", encoding="utf-8")
                run = subprocess.run(command + [str(bad)], capture_output=True, text=True)
                self.assertEqual(run.returncode, 1)
                self.assertEqual(json.loads(run.stdout)["status"], "error")


if __name__ == "__main__":
    unittest.main()
