"""
Bluestock Mutual Fund Analytics Capstone

This script loads cleaned and processed mutual fund datasets
into a SQLite database to support reporting, analysis, and
dashboard development.
"""

from sqlalchemy import create_engine
import pandas as pd


def load_database():
    """
    Load datasets into the SQLite database.

    The function reads raw and processed datasets and stores
    them as database tables in the Bluestock Mutual Fund
    Analytics database.

    Returns
    -------
    None
    """

    engine = create_engine(
        "sqlite:///data/db/bluestock_mf.db"
    )

    fund = pd.read_csv("data/raw/01_fund_master.csv")
    nav = pd.read_csv("data/processed/clean_nav_history.csv")
    txn = pd.read_csv("data/processed/clean_investor_transactions.csv")
    perf = pd.read_csv("data/processed/clean_scheme_performance.csv")
    aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

    fund.to_sql(
        "dim_fund",
        engine,
        if_exists="replace",
        index=False
    )

    nav.to_sql(
        "fact_nav",
        engine,
        if_exists="replace",
        index=False
    )

    txn.to_sql(
        "fact_transactions",
        engine,
        if_exists="replace",
        index=False
    )

    perf.to_sql(
        "fact_performance",
        engine,
        if_exists="replace",
        index=False
    )

    aum.to_sql(
        "fact_aum",
        engine,
        if_exists="replace",
        index=False
    )

    print("Database Loaded")


if __name__ == "__main__":
    load_database()