"""
Bluestock Mutual Fund Analytics Capstone

This script validates data consistency between the fund master
dataset and NAV history dataset by checking whether all AMFI
codes from the fund master are present in the NAV history data.
"""

import pandas as pd


def validate_amfi_codes():
    """
    Compare AMFI codes between fund master and NAV history datasets.

    The function identifies any AMFI codes that exist in the fund
    master dataset but are missing from the NAV history dataset.

    Returns
    -------
    None
    """

    fund_master = pd.read_csv("data/raw/01_fund_master.csv")
    nav_history = pd.read_csv("data/raw/02_nav_history.csv")

    master_codes = set(fund_master["amfi_code"])
    nav_codes = set(nav_history["amfi_code"])

    missing_codes = master_codes - nav_codes

    print(f"Fund Master Codes: {len(master_codes)}")
    print(f"NAV History Codes: {len(nav_codes)}")

    if len(missing_codes) == 0:
        print("\n✅ All AMFI codes exist in NAV history")
    else:
        print("\n❌ Missing Codes:")
        print(missing_codes)


if __name__ == "__main__":
    validate_amfi_codes()