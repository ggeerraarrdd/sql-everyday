# SQL Everyday \#068

## Monthly Merchant Balance

Site: DataLemur\
Difficulty per Site: Hard

## Problem

Say you have access to all the transactions for a given merchant account. Write a query to print the cumulative balance of the merchant account at the end of each day, with the total balance reset back to zero at the end of the month. Output the transaction date and cumulative balance. [[Full Description](https://datalemur.com/questions/sql-monthly-merchant-balance)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
  SELECT
    transaction_date::DATE AS date
    ,CASE WHEN type = 'deposit' THEN amount ELSE -amount END AS amnt 
  FROM transactions
),
  cte2 AS (
  SELECT
    date
    ,SUM(amnt) AS balance
  FROM cte1
  GROUP BY date
)
SELECT
  date
  ,SUM(balance) OVER (PARTITION BY DATE_TRUNC('month', date) ORDER BY date ASC) AS balance
FROM cte2
; 
```

## Site Solution

```sql
-- DataLemur Solution 
WITH daily_balances AS (
  SELECT
    DATE_TRUNC('day', transaction_date) AS transaction_day,
    DATE_TRUNC('month', transaction_date) AS transaction_month,
    SUM(CASE WHEN type = 'deposit' THEN amount
      WHEN type = 'withdrawal' THEN -amount END) AS balance
  FROM transactions
  GROUP BY 
    DATE_TRUNC('day', transaction_date),
    DATE_TRUNC('month', transaction_date))

SELECT
  transaction_day,
  SUM(balance) OVER (
    PARTITION BY transaction_month
    ORDER BY transaction_day) AS balance
FROM daily_balances
ORDER BY transaction_day;
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
