import argparse
import csv
from pathlib import Path


QUESTION = "Would you try another Python puzzle? Answer in your own words."
SAMPLE = Path(__file__).with_name("fictional_responses.csv")


def clean_answer(raw):
    # A phone keyboard may use a curly apostrophe for the same words.
    return raw.strip().lower().replace("’", "'")


def label_answer(clean):
    if clean in ("yes", "y"):
        return "yes"
    if clean in ("no", "n"):
        return "no"
    return "review"


def main():
    parser = argparse.ArgumentParser(description="Compare raw and cleaned survey answers.")
    parser.add_argument("csv_file", nargs="?", type=Path, default=SAMPLE)
    parser.add_argument("--raw", action="store_true", help="Show only the answers for the prediction game.")
    args = parser.parse_args()
    raw_answers = []
    counts = {"yes": 0, "no": 0, "review": 0}

    # Read just the poll question. The timestamp column can have any name.
    with args.csv_file.open(encoding="utf-8-sig", newline="") as source:
        rows = csv.DictReader(source)
        if QUESTION not in (rows.fieldnames or []):
            parser.error("The CSV must contain this question header: " + QUESTION)
        for row in rows:
            raw_answers.append(row[QUESTION] or "")

    if args.raw:
        for raw in raw_answers:
            print(repr(raw))
        return

    print("Raw answer -> cleaned text -> label")
    for raw in raw_answers:
        clean = clean_answer(raw)
        label = label_answer(clean)
        counts[label] += 1
        # repr shows the spaces inside the quotes.
        print(repr(raw), "->", repr(clean), "->", label)

    print("Exact 'yes' before cleaning:", raw_answers.count("yes"))
    print("After cleaning:", counts)


if __name__ == "__main__":
    main()
