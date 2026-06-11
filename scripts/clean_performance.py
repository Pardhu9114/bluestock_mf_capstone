"""
Bluestock Mutual Fund Analytics Capstone

This script cleans and validates mutual fund scheme performance
data by converting return columns to numeric format, identifying
expense ratio anomalies, and exporting the cleaned dataset for
further analysis.
"""

import pandas as pd


def clean_scheme_performance():
    """
    Clean and validate scheme performance data.

    The function converts return-related columns to numeric
    values, identifies schemes with unusual expense ratios,
    and saves the cleaned dataset for downstream analysis.

    Returns
    -------
    pandas.DataFrame
        Cleaned scheme performance dataset.
    """

    df = pd.read_csv("data/raw/07_scheme_performance.csv")

    return_cols = [
        "return_1yr_pct",
        "return_3yr_pct",
        "return_5yr_pct"
    ]

    for col in return_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    expense_anomalies = df[
        (df["expense_ratio_pct"] < 0.1)
        | (df["expense_ratio_pct"] > 2.5)
    ]

    print("Expense anomalies:")
    print(expense_anomalies)

    df.to_csv(
        "data/processed/clean_scheme_performance.csv",
        index=False
    )

    return df


if __name__ == "__main__":
    clean_scheme_performance()