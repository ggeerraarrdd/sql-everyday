# SQL Everyday \#019

## FAANG Stock Min-Max (Part 1)

Site: DataLemur\
Difficulty per Site: Medium

## Problem

The Bloomberg terminal is the go-to resource for financial professionals, offering convenient access to a wide array of financial datasets. As a Data Analyst at Bloomberg, you have access to historical data on stock performance.

Currently, you're analyzing the highest and lowest open prices for each FAANG stock by month over the years.

For each FAANG stock, display the ticker symbol, the month and year ('Mon-YYYY') with the corresponding highest and lowest open prices (refer to the Example Output format). Ensure that the results are sorted by ticker symbol. [[Full Description](https://datalemur.com/questions/sql-bloomberg-stock-min-max-1)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
  SELECT
    ticker
    ,MAX(open) AS open_max
    ,MIN(open) AS open_min
  FROM stock_prices
  GROUP BY ticker
)
SELECT
  cte1.ticker AS ticker
  ,TO_CHAR(sp1.date, 'Mon-YYYY') AS highest_mth
  ,cte1.open_max AS highest_open
  ,TO_CHAR(sp2.date, 'Mon-YYYY') AS lowest_mth
  ,cte1.open_min AS lowest_open
FROM cte1
JOIN stock_prices AS sp1 ON cte1.ticker = sp1.ticker AND cte1.open_max = sp1.open
JOIN stock_prices AS sp2 ON cte1.ticker = sp2.ticker AND cte1.open_min = sp2.open
ORDER BY ticker ASC
;
```

## Site Solution

```sql
-- DataLemur Solution 
WITH highest_prices AS (
  SELECT 
    ticker,
    TO_CHAR(date, 'Mon-YYYY') AS highest_mth,
    MAX(open) AS highest_open,
    ROW_NUMBER() OVER (PARTITION BY ticker ORDER BY open DESC) AS row_num
  FROM stock_prices
  GROUP BY ticker, TO_CHAR(date, 'Mon-YYYY'), open
),
lowest_prices AS (
  SELECT 
    ticker,
    TO_CHAR(date, 'Mon-YYYY') AS lowest_mth,
    MIN(open) AS lowest_open,
    ROW_NUMBER() OVER (PARTITION BY ticker ORDER BY open) AS row_num
  FROM stock_prices
  GROUP BY ticker, TO_CHAR(date, 'Mon-YYYY'), open
)

SELECT
  highest.ticker,
  highest.highest_mth,
  highest.highest_open,
  lowest.lowest_mth,
  lowest.lowest_open
FROM highest_prices as highest
INNER JOIN lowest_prices AS lowest
  ON highest.ticker = lowest.ticker
  AND highest.row_num = 1 -- Highest open price
  AND lowest.row_num = 1 -- Lowest open price
ORDER BY highest.ticker;
```

## Notes

TODO

## NB

TBD

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
