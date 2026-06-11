"""
Bluestock Mutual Fund Analytics Capstone

This script cleans and preprocesses mutual fund NAV history data
by converting date fields, sorting records, removing duplicates,
validating NAV values, handling missing data, and exporting the
cleaned dataset for further analysis.
"""

import pandas as pd


def clean_nav_history():
    """
    Clean and preprocess NAV history data.

    The function converts date columns to datetime format,
    sorts records by fund and date, removes duplicate entries,
    filters invalid NAV values, forward-fills missing NAV data
    within each fund, and saves the cleaned dataset.

    Returns
    -------
    pandas.DataFrame
        Cleaned NAV history dataset.
    """

    df = pd.read_csv("data/raw/02_nav_history.csv")

    # Convert date
    df["date"] = pd.to_datetime(df["date"])

    # Sort records
    df = df.sort_values(["amfi_code", "date"])

    # Remove duplicates
    df = df.drop_duplicates()

    # Validate NAV values
    df = df[df["nav"] > 0]

    # Forward fill NAV within each fund
    df["nav"] = df.groupby("amfi_code")["nav"].ffill()

    # Save cleaned dataset
    df.to_csv("data/processed/clean_nav_history.csv", index=False)

    print(df.shape)

    return df


if __name__ == "__main__":
    clean_nav_history()