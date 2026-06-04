-- 1. Top 5 funds by AUM
SELECT *
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per month
SELECT
strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

-- 3. SIP Inflow YoY Growth
SELECT *
FROM fact_sip_industry;

-- 4. Transactions by State
SELECT
state,
COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY state
ORDER BY transaction_count DESC;

-- 5. Funds with Expense Ratio < 1%
SELECT
scheme_name,
expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1;

-- 6. Fund Count by Category
SELECT
category,
COUNT(*) AS fund_count
FROM dim_fund
GROUP BY category;

-- 7. Top 5 Funds by Sharpe Ratio
SELECT
scheme_name,
sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- 8. Top 5 Funds by Alpha
SELECT
scheme_name,
alpha
FROM fact_performance
ORDER BY alpha DESC
LIMIT 5;

-- 9. Average Transaction Amount by State
SELECT
state,
AVG(amount_inr) AS avg_amount
FROM fact_transactions
GROUP BY state;

-- 10. Number of Transactions by Type
SELECT
transaction_type,
COUNT(*) AS count
FROM fact_transactions
GROUP BY transaction_type;