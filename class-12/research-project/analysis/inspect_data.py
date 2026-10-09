"""Inspect the original export without changing it."""

import pandas as pd

from settings import DATA_FILE, DATA_LABEL


def main():
    # Explicit text types preserve identifiers such as a code starting with zero.
    data = pd.read_csv(DATA_FILE, dtype={"session_code": str, "participant_code": str})
    print(DATA_LABEL)
    print("First five rows:")
    print(data.head().to_string(index=False))
    print("\nRows and columns:", data.shape)
    print("\nColumn types:")
    print(data.dtypes)
    print("\nBlank cells per column:")
    print(data.isna().sum())
    people = data[["session_code", "participant_code"]].drop_duplicates()
    print("\nParticipants in this export:", len(people))


if __name__ == "__main__":
    main()
