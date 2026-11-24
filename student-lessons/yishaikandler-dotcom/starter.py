import csv
from collections import Counter
from pathlib import Path


def clean_text(text):
    # TODO 1: Remove surrounding whitespace.
    text = text
    # TODO 2: Convert letters to lowercase.
    text = text
    # TODO 3: Remove exclamation marks.
    text = text
    return text


def show_counts(title, counts):
    print(f"{title} | {len(counts)} categories | {sum(counts.values())} responses")
    for label, count in sorted(counts.items()):
        print(f"  {label!r}: {count}")


def report(cleaner):
    survey = Path(__file__).with_name("survey_responses.csv")
    with survey.open(encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))

    for column in ("uses_ai", "favorite_tool"):
        before = Counter()
        after = Counter()
        for row in rows:
            label = row[column]
            before[label] += 1
            after[cleaner(label)] += 1
        print(f"\n{column}")
        show_counts("BEFORE", before)
        show_counts("AFTER", after)


if __name__ == "__main__":
    report(clean_text)
