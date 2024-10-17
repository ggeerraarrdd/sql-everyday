# SQL Everyday \#020

## Y-on-Y Growth Rate

Site: DataLemur\
Difficulty per Site: Hard

## Problem

Assume you're given a table containing information about Wayfair user transactions for different products. Write a query to calculate the year-on-year growth rate for the total spend of each product, grouping the results by product ID.

The output should include the year in ascending order, product ID, current year's spend, previous year's spend and year-on-year growth percentage, rounded to 2 decimal places. [[Full Description](https://datalemur.com/questions/yoy-growth-rate)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT 
    product_id
    ,EXTRACT(YEAR FROM transaction_date) AS year
    ,SUM(spend) AS total_spend
  FROM user_transactions
  GROUP BY product_id, year
)
SELECT
  year
  ,product_id
  ,total_spend AS cur_year_spend
  ,LAG(total_spend, 1) OVER (PARTITION BY product_id ORDER BY product_id, year) AS prev_year_spend
  ,ROUND(total_spend / LAG(total_spend, 1) OVER (PARTITION BY product_id ORDER BY product_id, year) * 100 - 100, 2) AS yoy_rate
FROM cte 
;
```

## Site Solution

```sql
-- DataLemur Solution 
WITH yearly_spend_cte AS (
  SELECT 
    EXTRACT(YEAR FROM transaction_date) AS yr,
    product_id,
    spend AS curr_year_spend,
    LAG(spend) OVER (
      PARTITION BY product_id 
      ORDER BY 
        product_id, 
        EXTRACT(YEAR FROM transaction_date)) AS prev_year_spend 
  FROM user_transactions
)

SELECT 
  yr,
  product_id, 
  curr_year_spend, 
  prev_year_spend, 
  ROUND(100 * 
    (curr_year_spend - prev_year_spend)
    / prev_year_spend
  , 2) AS yoy_rate 
FROM yearly_spend_cte;
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
