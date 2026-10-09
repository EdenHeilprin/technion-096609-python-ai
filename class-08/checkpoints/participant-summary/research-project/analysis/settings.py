"""Choose one data source for all analyses in this project."""

from pathlib import Path

# Start from this file's location, so Run Python File works from any folder.
PROJECT_DIR = Path(__file__).resolve().parents[1]

# For a classroom export, change these three lines together. Keep the original CSV.
DATA_FILE = PROJECT_DIR / "data" / "synthetic_choices.csv"
DATA_LABEL = "Synthetic teaching example"
IS_SYNTHETIC = True

# A different input filename gets its own output folder, avoiding mixed results.
OUTPUT_DIR = PROJECT_DIR / "outputs" / DATA_FILE.stem
