# SQL Everyday \#062

## FAANG Underperforming Stocks (Part 3)

Site: DataLemur\
Difficulty per Site: Hard

## Problem

As a trading analyst at Bloomberg, your task is to identify specific months when a majority of the FAANG stocks (Facebook, Amazon, Apple, Netflix, Google) experienced a gain in value compared to the previous month, while one stock lagged behind its peers by recording a decrease in value. This analysis involves comparing opening prices from the previous month.

In essence, you're seeking months where 5 out of 6 FAANG stocks demonstrated an increase in value with one stock experiencing a decline.

Write a query to display the month and year in 'Mon-YYYY' format along with the ticker symbol of the stock that underperformed relative to its peers, ordered by month and year (in 'Mon-YYYY' format). [[Full Description](https://datalemur.com/questions/sql-bloomberg-underperforming-stocks)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
  SELECT
    date
    ,ticker
    ,open
    ,open - LAG(open, 1) OVER (PARTITION BY ticker ORDER BY date ASC) AS lag_open
  FROM stock_prices
),
cte2 AS (
  SELECT
    *
    ,ROW_NUMBER() OVER (PARTITION BY date ORDER BY ticker ASC) AS rownum
  FROM cte1
  WHERE lag_open < 0
),
cte3 AS (
  SELECT
    *
    ,LEAD(rownum, 1) OVER (PARTITION BY date ORDER BY date ASC) AS lag_row
  FROM cte2
)
SELECT
  TO_CHAR(date, 'Mon-YYYY') AS mth_yr
  ,ticker AS underperforming_stock
FROM cte3
WHERE rownum = 1
  AND lag_row IS NULL
ORDER BY date ASC
;
```

## Site Solution

```sql
-- DataLemur Solution 
WITH monthly_changes AS ( -- CTE using Step 1's query
  SELECT
    TO_CHAR(date, 'Mon-YYYY') AS mth_yr,
    ticker,
    LAG(open) OVER (
      PARTITION BY ticker ORDER BY date) AS prev_open,
    open AS curr_open
  FROM stock_prices 
)
, monthly_gains AS ( -- CTE using Step 2's query
SELECT
  mth_yr,
  ticker,
  CASE WHEN curr_open > prev_open THEN 1 ELSE 0 END AS gain_count
FROM monthly_changes
)
, stock_summary AS ( -- CTE using Step 3's query
  SELECT 
    mth_yr,
    ticker,
    SUM(gain_count) OVER (PARTITION BY mth_yr) AS total_gains,
    CASE WHEN SUM(gain_count) OVER (PARTITION BY mth_yr) = 5 
      AND gain_count = 0 THEN ticker ELSE NULL 
    END AS underperforming_stock
  FROM monthly_gains
)

SELECT 
  mth_yr,
  underperforming_stock
FROM stock_summary
WHERE total_gains = 5
  AND underperforming_stock IS NOT NULL
ORDER BY mth_yr;
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
