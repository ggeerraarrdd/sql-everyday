# SQL Everyday \#185

## Sales Analysis I

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution that reports the best **seller** by total sales price, If there is a tie, report them all.

Return the resulting table in **any order**. [[Full Description](https://leetcode.com/problems/sales-analysis-i/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
    SELECT
        seller_id
        ,RANK() OVER (ORDER BY SUM(price) DESC) AS rank_total
    FROM Sales
    GROUP BY seller_id
)
SELECT
    seller_id
FROM cte
WHERE rank_total = 1
;
```

## Site Solution

```sql
-- LeetCode Solution 
WITH aggregated_sales AS (
  SELECT 
    seller_id, 
    SUM(price) AS total_price 
  FROM 
    Sales 
  GROUP BY 
    seller_id
) 
SELECT 
  seller_id 
FROM 
  aggregated_sales 
WHERE 
  total_price = (
    SELECT 
      MAX(total_price) 
    FROM 
      aggregated_sales
  );

-- Code Author: Brian
-- https://leetcode.com/problems/sales-analysis-i/solutions/311519/mysql-solution
SELECT seller_id
FROM Sales
GROUP BY seller_id
HAVING SUM(PRICE) >= all (
    SELECT SUM(PRICE)
    FROM Sales
    GROUP BY seller_id
)
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
