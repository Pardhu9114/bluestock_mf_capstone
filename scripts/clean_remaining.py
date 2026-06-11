"""
Bluestock Mutual Fund Analytics Capstone

This script performs basic data cleaning on multiple raw datasets
by removing duplicate records and saving the cleaned versions
to the processed data directory.
"""

import pandas as pd


def clean_datasets():
    """
    Clean multiple datasets by removing duplicate records.

    The function reads each dataset from the raw data directory,
    removes duplicate rows, saves the cleaned dataset to the
    processed data directory, and displays the output filename.

    Returns
    -------
    None
    """

    files = [
        "01_fund_master.csv",
        "03_aum_by_fund_house.csv",
        "04_monthly_sip_inflows.csv",
        "05_category_inflows.csv",
        "06_industry_folio_count.csv",
        "09_portfolio_holdings.csv",
        "10_benchmark_indices.csv"
    ]

    for file in files:
        df = pd.read_csv(f"data/raw/{file}")

        # Remove duplicate records
        df = df.drop_duplicates()

        output = file.replace(".csv", "_clean.csv")

        # Save cleaned dataset
        df.to_csv(
            f"data/processed/{output}",
            index=False
        )

        print(output)


if __name__ == "__main__":
    clean_datasets()