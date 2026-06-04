# Mutual Fund Analytics Data Dictionary

## 01_fund_master.csv

| Column | Type | Description |
|----------|--------|------------|
| amfi_code | TEXT | Unique AMFI scheme code |
| fund_house | TEXT | Mutual fund company |
| scheme_name | TEXT | Official scheme name |
| category | TEXT | Equity, Debt, Hybrid |
| sub_category | TEXT | Large Cap, Mid Cap, Small Cap, etc |
| risk_category | TEXT | Low, Moderate, High, Very High |

---

## 02_nav_history.csv

| Column | Type | Description |
|----------|--------|------------|
| amfi_code | TEXT | Fund identifier |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |

---

## 03_aum_by_fund_house.csv

| Column | Type | Description |
|----------|--------|------------|
| fund_house | TEXT | AMC Name |
| aum_crore | REAL | Assets under Management in crore |

---

## 08_investor_transactions.csv

| Column | Type | Description |
|----------|--------|------------|
| investor_id | TEXT | Unique investor ID |
| transaction_date | DATE | Transaction date |
| transaction_type | TEXT | SIP, Lumpsum, Redemption |
| amount_inr | REAL | Transaction amount |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| kyc_status | TEXT | Verified or Pending |

---

Source:
AMFI India, mfapi.in, Bluestock Capstone Datasets