"""
Bluestock Mutual Fund Analytics Capstone

This script performs an initial exploratory review of all raw
CSV datasets by displaying dataset dimensions, data types,
sample records, and missing value statistics.
"""

from pathlib import Path
import pandas as pd


def inspect_raw_datasets():
    """
    Inspect all raw CSV datasets.

    The function scans the raw data directory, reads each CSV
    file, and displays key information including dataset shape,
    column data types, sample records, and missing value counts.

    Returns
    -------
    None
    """

    raw_folder = Path("data/raw")

    csv_files = sorted(raw_folder.glob("*.csv"))

    print(f"Found {len(csv_files)} CSV files\n")

    for file in csv_files:
        print("=" * 80)
        print(f"FILE: {file.name}")

        try:
            df = pd.read_csv(file)

            print("\nShape:")
            print(df.shape)

            print("\nData Types:")
            print(df.dtypes)

            print("\nFirst 5 Rows:")
            print(df.head())

            print("\nMissing Values:")
            print(df.isnull().sum())

        except Exception as e:
            print(f"Error reading {file.name}: {e}")

        print("\n")


if __name__ == "__main__":
    inspect_raw_datasets()