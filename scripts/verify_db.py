from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///data/db/bluestock_mf.db")

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