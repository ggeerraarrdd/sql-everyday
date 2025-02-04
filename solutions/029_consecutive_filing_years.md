# SQL Everyday \#029

## Consecutive Filing Years

Site: DataLemur\
Difficulty per Site: Hard

## Problem

Intuit, a company known for its tax filing products like TurboTax and QuickBooks, offers multiple versions of these products.

Write a query that identifies the user IDs of individuals who have filed their taxes using any version of TurboTax for three or more consecutive years. Each user is allowed to file taxes once a year using a specific product. Display the output in the ascending order of user IDs. [[Full Description](https://datalemur.com/questions/consecutive-filing-years)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
  SELECT
    user_id
    ,filing_date
    ,EXTRACT(YEAR FROM filing_date) AS year
    ,EXTRACT(YEAR FROM LAG(filing_date, 1) OVER (PARTITION BY user_id ORDER BY filing_date DESC)) AS year_lag
  FROM filed_taxes
  WHERE product LIKE '%TurboTax%'
),
cte2 AS (
SELECT
    *
    ,year - COALESCE(year_lag, year) AS year_diff
    ,ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY year DESC) AS rownum
  FROM cte1
)
SELECT
  DISTINCT user_id
FROM cte2
WHERE rownum = 3 AND year_diff = -1
;
```

## Site Solution

```sql
-- DataLemur Solution 
WITH turbotax_filings_cte AS (
  SELECT
    user_id,
      DATE_TRUNC('year', filing_date) AS filing_year,
      LAG(DATE_TRUNC('year', filing_date)) OVER (
        PARTITION BY user_id 
        ORDER BY filing_date) AS previous_year,
      LEAD(DATE_TRUNC('year', filing_date)) OVER (
        PARTITION BY user_id 
        ORDER BY filing_date) AS following_year
  FROM filed_taxes
  WHERE LOWER(product) LIKE 'turbotax%'
)

SELECT user_id
FROM turbotax_filings_cte
WHERE previous_year = filing_year - interval '1 year'
  OR following_year = filing_year + interval '1 year'
GROUP BY user_id
HAVING COUNT(filing_year) >= 3;
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
