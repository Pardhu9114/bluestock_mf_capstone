"""
Bluestock Mutual Fund Analytics Capstone

This script explores the fund master dataset by displaying
unique values for key categorical fields and summarizing
the total number of unique AMFI codes.
"""

import pandas as pd


def analyze_fund_master():
    """
    Analyze key attributes of the fund master dataset.

    The function displays unique fund houses, categories,
    sub-categories, risk categories, and the total number
    of unique AMFI codes available in the dataset.

    Returns
    -------
    None
    """

    df = pd.read_csv("data/raw/01_fund_master.csv")

    print("\n===== UNIQUE FUND HOUSES =====")
    print(df["fund_house"].unique())

    print("\n===== UNIQUE CATEGORIES =====")
    print(df["category"].unique())

    print("\n===== UNIQUE SUB-CATEGORIES =====")
    print(df["sub_category"].unique())

    print("\n===== UNIQUE RISK CATEGORIES =====")
    print(df["risk_category"].unique())

    print("\n===== TOTAL AMFI CODES =====")
    print(df["amfi_code"].nunique())


if __name__ == "__main__":
    analyze_fund_master()