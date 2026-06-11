"""
Bluestock Mutual Fund Analytics Capstone

This script validates the SQLite database by checking the
record count of each table loaded during the ETL process.
It helps verify that data has been successfully imported
into the database.
"""

from sqlalchemy import create_engine
import pandas as pd


def validate_database_tables():
    """
    Validate database tables by displaying row counts.

    The function connects to the SQLite database, retrieves
    the number of records from each table, and displays the
    results for verification purposes.

    Returns
    -------
    None
    """

    engine = create_engine(
        "sqlite:///data/db/bluestock_mf.db"
    )

    tables = [
        "dim_fund",
        "fact_nav",
        "fact_transactions",
        "fact_performance",
        "fact_aum"
    ]

    for table in tables:
        count = pd.read_sql(
            f"SELECT COUNT(*) as rows FROM {table}",
            engine
        )

        print(table)
        print(count)
        print()


if __name__ == "__main__":
    validate_database_tables()