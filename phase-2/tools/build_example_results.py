"""Rebuild shareable reference outputs from the explicitly synthetic fixture only."""
import sys
from pathlib import Path

PHASE = Path(__file__).resolve().parents[1]
PROJECT = PHASE / "project"
sys.path.insert(0, str(PROJECT / "analysis"))
from analyze_choices import run_analysis

destination = PHASE / "example-results"
summary = run_analysis(PROJECT / "data/synthetic_choices.csv", destination,
                       "Synthetic teaching example", True)
if (summary["included_participants"], summary["included_trials"], summary["gamble_count"]) != (15, 90, 46):
    raise SystemExit("Synthetic reference drifted; review before publishing.")
(destination / "README.md").write_text(
    "# Synthetic reference results\n\nGenerated from the supplied fictional data by "
    "analysis/analyze_choices.py. These are not student responses. "
    "summary.json identifies the exact source by SHA-256. Run the script in your own project "
    "to regenerate the same calculations.\n", encoding="utf-8")
