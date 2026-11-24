import ast
import csv
import re
import subprocess
import sys
import unittest
from collections import Counter
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from instructor.survey_solution import clean_text


def run(*args, cwd=ROOT):
    return subprocess.run(
        [sys.executable, "-B", *args], cwd=cwd, check=True,
        capture_output=True, text=True,
    ).stdout


class WorkshopTests(unittest.TestCase):
    def test_syntax(self):
        for path in ROOT.rglob("*.py"):
            with self.subTest(path=path):
                ast.parse(path.read_text(encoding="utf-8"))

    def test_demo_from_another_folder(self):
        with TemporaryDirectory() as folder:
            lines = run(str(ROOT / "demo.py"), cwd=folder).splitlines()
        self.assertEqual(lines, [
            "Original: ' CLAUDE!! '", "After strip: 'CLAUDE!!'",
            "After lower: 'claude!!'", "After replace: 'claude'",
            "Original again: ' CLAUDE!! '",
        ])

    def test_practice(self):
        self.assertEqual(len(run("practice.py").splitlines()), 4)
        self.assertEqual(run("instructor/practice_solution.py").splitlines(),
                         ["'study group'", "'gemini'", "'yes'", "'chatgpt'"])

    def test_survey(self):
        with (ROOT / "survey_responses.csv").open(encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            self.assertEqual(reader.fieldnames, ["student_id", "uses_ai", "favorite_tool"])
            rows = list(reader)
        self.assertEqual(len(rows), 40)
        self.assertEqual(len({row["student_id"] for row in rows}), 40)
        expected = {
            "uses_ai": {"yes": 32, "no": 8},
            "favorite_tool": {"chatgpt": 16, "claude": 8, "gemini": 8, "none": 8},
        }
        for row in rows:
            self.assertEqual(clean_text(row["uses_ai"]) == "no",
                             clean_text(row["favorite_tool"]) == "none")
        starter_output = run("starter.py")
        solution_output = run("-m", "instructor.survey_solution")
        for column, counts in expected.items():
            raw = Counter(row[column] for row in rows)
            clean = Counter(clean_text(row[column]) for row in rows)
            self.assertEqual(clean, counts)
            self.assertEqual(sum(clean.values()), sum(raw.values()))
            for output, after in [(starter_output, raw), (solution_output, clean)]:
                block = [column]
                for title, table in [("BEFORE", raw), ("AFTER", after)]:
                    block.append(f"{title} | {len(table)} categories | 40 responses")
                    block.extend(f"  {label!r}: {n}" for label, n in sorted(table.items()))
                self.assertIn("\n".join(block), output)

    def test_bonus(self):
        self.assertEqual(run("regex_bonus.py").splitlines(), ["0541234567"] * 3)

    def test_readme_files(self):
        guide = (ROOT / "README.md").read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", guide):
            if not target.startswith(("https://", "#")):
                self.assertTrue((ROOT / target.split("#")[0]).is_file(), target)
        for name in re.findall(r'python ([\w]+\.py)', guide):
            self.assertTrue((ROOT / name).is_file(), name)


if __name__ == "__main__":
    unittest.main()
