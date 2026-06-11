"""
Bluestock Mutual Fund Analytics Capstone

This script retrieves historical NAV data for selected mutual
fund schemes using the MFAPI service and stores the data as
CSV files for further analysis.
"""

import pandas as pd
import requests


def fetch_nav_data():
    """
    Fetch historical NAV data for selected mutual fund schemes.

    The function retrieves NAV history from the MFAPI endpoint
    for predefined mutual fund schemes and saves each dataset
    as a CSV file in the raw data directory.

    Returns
    -------
    None
    """

    schemes = {
        "hdfc_top100": 125497,
        "sbi_bluechip": 119551,
        "icici_bluechip": 120503,
        "nippon_largecap": 118632,
        "axis_bluechip": 119092,
        "kotak_bluechip": 120841
    }

    for name, code in schemes.items():

        url = f"https://api.mfapi.in/mf/{code}"

        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            nav_df = pd.DataFrame(data["data"])

            filename = f"data/raw/{name}_nav.csv"

            nav_df.to_csv(filename, index=False)

            print(f"Saved {filename}")

        else:
            print(f"Failed: {name}")


if __name__ == "__main__":
    fetch_nav_data()