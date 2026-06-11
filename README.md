# Bluestock Mutual Fund Analytics Capstone

## Project Overview

The Bluestock Mutual Fund Analytics Platform is an end-to-end data analytics solution designed to analyze mutual fund performance, investor behavior, and industry trends. The project integrates data ingestion, ETL processing, database management, advanced analytics, and dashboard visualization to generate actionable investment insights.

## Objectives

* Build an ETL pipeline for mutual fund datasets
* Clean and validate financial data
* Store processed data in SQLite
* Perform exploratory data analysis (EDA)
* Calculate mutual fund performance metrics
* Develop a recommendation engine
* Build an interactive Power BI dashboard
* Generate business insights for investors

## Tech Stack

* Python
* Pandas
* NumPy
* SQLAlchemy
* SQLite
* Jupyter Notebook
* Power BI
* Git & GitHub

## Project Structure

```text
bluestock_mf_capstone/
├── dashboard/
├── data/
├── notebooks/
├── reports/
├── scripts/
├── sql/
├── README.md
├── requirements.txt
```

## Data Sources

* Mutual Fund NAV Data
* Fund Master Dataset
* Investor Transactions
* AUM Data
* Portfolio Holdings
* Benchmark Index Data
* MFAPI Historical NAV Data

## ETL Workflow

1. Data Ingestion
2. Data Cleaning
3. Data Validation
4. Database Loading
5. Analytics Processing
6. Dashboard Visualization

## Database Tables

* dim_fund
* fact_nav
* fact_transactions
* fact_performance
* fact_aum

## Analytics Performed

* CAGR Analysis
* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown
* Benchmark Comparison

## Dashboard Features

* Fund Performance Tracking
* AUM Growth Analysis
* SIP Trend Monitoring
* Risk Metrics Visualization
* Investor Participation Insights

## How to Run

```bash
source venv/Scripts/activate

python scripts/amfi_validation.py
python scripts/clean_nav_history.py
python scripts/load_sqlite.py
python scripts/verify_db.py
```

## GitHub Repository

Repository:
https://github.com/Pardhu9114/bluestock_mf_capstone

Version:
v1.0

## Author

CH V S Pardhu
