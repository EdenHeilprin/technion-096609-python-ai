"""Provided data checks. The lessons focus on the analysis that follows them."""

import csv
from pathlib import Path

import pandas as pd


COLUMNS = [
    "session_code", "participant_code", "study_version", "round_number",
    "sure_points", "gamble_high", "gamble_probability", "choice", "confidence",
]
PERSON_COLUMNS = ["session_code", "participant_code"]
OFFERS = {1: 2, 2: 3, 3: 4, 4: 6, 5: 7, 6: 8}


def read_export(path):
    """Read a full-v1 custom export; stop on malformed data instead of guessing."""
    path = Path(path)
    if not path.is_file():
        raise ValueError(f"Data file not found: {path}. Check analysis/settings.py.")

    # Check the original header before pandas can rename duplicate column names.
    with path.open(encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file)
        header = next(reader, [])
        if header != COLUMNS:
            raise ValueError("Expected the full-v1 custom export columns, in their original order. See data/CODEBOOK.md.")
        for line_number, row in enumerate(reader, start=2):
            if len(row) != len(COLUMNS):
                raise ValueError(f"CSV line {line_number} has {len(row)} fields; expected {len(COLUMNS)}.")

    # Keep codes as text and empty cells as empty strings, not accidental numbers.
    data = pd.read_csv(path, dtype=str, keep_default_na=False, encoding="utf-8-sig")
    if data.empty:
        raise ValueError("This export contains no participant rows.")
    for column in PERSON_COLUMNS:
        if data[column].str.strip().eq("").any():
            raise ValueError(f"Missing {column}; each row needs a participant identity.")
        if data[column].ne(data[column].str.strip()).any():
            raise ValueError(f"Unexpected whitespace in {column}; check the original export.")
    if not data["study_version"].eq("full-v1").all():
        raise ValueError("Analyze full-v1 only. Do not mix the one-round or modified study with this export.")

    # Convert numeric columns only after checking that every required value is numeric.
    for column in ["round_number", "sure_points", "gamble_high", "gamble_probability"]:
        numeric = pd.to_numeric(data[column], errors="coerce")
        if numeric.isna().any():
            raise ValueError(f"Missing or nonnumeric value in {column}.")
        data[column] = numeric
    if not data["round_number"].isin(OFFERS).all():
        raise ValueError("Round numbers must be whole numbers from 1 to 6.")
    data["round_number"] = data["round_number"].astype(int)

    key = PERSON_COLUMNS + ["round_number"]
    if data.duplicated(key).any():
        raise ValueError("Duplicate participant/round row. Do not concatenate overlapping exports or silently drop duplicates.")
    expected_offers = data["round_number"].map(OFFERS)
    if not data["sure_points"].eq(expected_offers).all():
        raise ValueError("Sure offers do not match full-v1's fixed six-round order.")
    if not data["gamble_high"].eq(10).all() or not data["gamble_probability"].eq(0.5).all():
        raise ValueError("The gamble must be a 50% chance of 10 points (otherwise 0).")
    if not data["choice"].isin(["sure", "gamble", ""]).all():
        raise ValueError("Choice must be sure, gamble, or blank for an unanswered round.")

    # An unanswered row has two blank response fields. It is not a sure choice or 0 confidence.
    missing_choice = data["choice"].eq("")
    missing_confidence = data["confidence"].eq("")
    if not missing_choice.eq(missing_confidence).all():
        raise ValueError("Choice and confidence must both be present, or both blank for an unanswered round.")
    confidence = pd.to_numeric(data["confidence"].replace("", pd.NA), errors="coerce")
    answered = ~missing_choice
    valid_confidence = confidence.between(1, 7) & confidence.mod(1).eq(0)
    if not valid_confidence[answered].fillna(False).all():
        raise ValueError("Answered rounds require whole-number confidence from 1 to 7.")
    data["confidence"] = confidence.astype("Int64")
    data["sure_points"] = data["sure_points"].astype(int)
    return data.sort_values(key).reset_index(drop=True)


def select_complete_participants(data):
    """Return eligible trials and a report for every participant, including exclusions."""
    rows = []
    for (session_code, participant_code), person in data.groupby(PERSON_COLUMNS, sort=True):
        observed_rounds = set(person["round_number"])
        answered_rounds = int(person["choice"].ne("").sum())
        included = observed_rounds == set(OFFERS) and answered_rounds == 6
        missing = sorted(set(OFFERS) - observed_rounds)
        reasons = []
        if missing:
            reasons.append("missing rounds " + ", ".join(map(str, missing)))
        if answered_rounds != len(person):
            reasons.append(f"{len(person) - answered_rounds} unanswered rounds")
        rows.append({
            "session_code": session_code,
            "participant_code": participant_code,
            "rows_present": len(person),
            "answered_rounds": answered_rounds,
            "included": included,
            "reason": "included: six complete rounds" if included else "; ".join(reasons),
        })
    report = pd.DataFrame(rows)
    # Join on both codes: the same participant label in different sessions is not one person.
    eligible_keys = report.loc[report["included"], PERSON_COLUMNS]
    clean = data.merge(eligible_keys, on=PERSON_COLUMNS, how="inner", validate="many_to_one")
    return clean.copy(), report
