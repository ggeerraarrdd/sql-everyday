# SQL Everyday \#005

## Highest-Grossing Items

Site: DataLemur\
Difficulty per Site: Medium

## Problem

Write a query to obtain a breakdown of the time spent sending vs. opening snaps as a percentage of total time spent on these activities grouped by age group. Round the percentage to 2 decimal places in the output. [[Full Description](https://datalemur.com/questions/time-spent-snaps)]

## Solution

```sql
-- Submitted Solution
WITH cte1 AS (
  SELECT 
    category
    ,product
    ,SUM(spend) AS total_spend
  FROM product_spend
  WHERE EXTRACT(YEAR FROM transaction_date) = 2022
  GROUP BY category, product
  ORDER BY category, total_spend DESC
),
cte2 AS (
  SELECT
    category
    ,product
    ,total_spend
    ,DENSE_RANK() OVER (PARTITION BY category ORDER BY total_spend DESC) AS cat_rank
  FROM cte1
)
SELECT
  category
  ,product
  ,total_spend
FROM cte2
WHERE cat_rank < 3
ORDER BY category, cat_rank
;

-- DataLemur Solution
WITH ranked_spending_cte AS (
  SELECT 
    category, 
    product, 
    SUM(spend) AS total_spend,
    RANK() OVER (PARTITION BY category ORDER BY SUM(spend) DESC) AS ranking 
  FROM product_spend
  WHERE EXTRACT(YEAR FROM transaction_date) = 2022
  GROUP BY category, product
)
SELECT 
  category, 
  product, 
  total_spend 
FROM ranked_spending_cte 
WHERE ranking <= 2 
ORDER BY category, ranking;
```

## Notes

* This is a classic SQL ranking problem requiring a window function and a CTE or nested subquery (but always go with a CTE for readability).
* The key is knowing the difference between [`RANK()` and `DENSE_RANK`](https://www.google.com/search?q=rank()+vs+dense_rank()).
* New to me: You can use an aggregate function in the `OVER()` clause of window function. This would have eliminated one CTE in my submitted solution.

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
