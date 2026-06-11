"""
Bluestock Mutual Fund Analytics Capstone

This script cleans and validates investor transaction data by
standardizing transaction types, validating transaction amounts
and KYC status, and exporting the cleaned dataset for further
analysis.
"""

import pandas as pd


def clean_investor_transactions():
    """
    Clean and validate investor transaction data.

    The function converts transaction dates to datetime format,
    standardizes transaction type values, filters invalid
    transaction records, validates KYC status, and saves the
    cleaned dataset.

    Returns
    -------
    pandas.DataFrame
        Cleaned investor transaction dataset.
    """

    df = pd.read_csv("data/raw/08_investor_transactions.csv")

    # Convert transaction date
    df["transaction_date"] = pd.to_datetime(df["transaction_date"])

    # Standardize transaction type values
    df["transaction_type"] = (
        df["transaction_type"]
        .str.strip()
        .str.title()
    )

    # Keep only valid transaction types
    valid_types = ["Sip", "Lumpsum", "Redemption"]
    df = df[df["transaction_type"].isin(valid_types)]

    # Keep positive transaction amounts
    df = df[df["amount_inr"] > 0]

    # Validate KYC status
    valid_kyc = ["Verified", "Pending"]
    df = df[df["kyc_status"].isin(valid_kyc)]

    # Save cleaned dataset
    df.to_csv(
        "data/processed/clean_investor_transactions.csv",
        index=False
    )

    print(df.shape)

    return df


if __name__ == "__main__":
    clean_investor_transactions()