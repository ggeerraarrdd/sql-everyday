# SQL Everyday \#056

## Follow-Up Airpod Percentage

Site: DataLemur\
Difficulty per Site: Hard

## Problem

The Apple retention team needs your help to investigate buying patterns. Write a query to determine the percentage of buyers who bought AirPods directly after they bought iPhones. Round your answer to a percentage (i.e. 20 for 20%, 50 for 50) with no decimals. [[Full Description](https://datalemur.com/questions/follow-up-airpod-percentage)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
SELECT
  customer_id
  ,product_name AS product_1
  ,LEAD(product_name, 1) OVER (PARTITION BY customer_id ORDER BY transaction_id ASC) AS product_2
FROM transactions
)
SELECT
  ROUND(100.0 * SUM(CASE WHEN product_1 = 'iPhone' AND product_2 = 'AirPods' THEN 1 ELSE 0 END) / COUNT(DISTINCT customer_id), 0) AS counted
FROM cte
;
```

## Site Solution

```sql
-- DataLemur Solution 
WITH lag_products AS (
  SELECT
  customer_id,
  product_name,
  LAG(product_name)
    OVER(PARTITION BY customer_id
    ORDER BY transaction_timestamp) AS prev_prod
  FROM transactions
  GROUP BY
  customer_id,
  product_name,
  transaction_timestamp
),
interested_users AS (
  SELECT customer_id AS airpod_iphone_buyers
  FROM lag_products
  WHERE LOWER(product_name) = 'airpods'
    AND LOWER(prev_prod) = 'iphone'
  GROUP BY customer_id
)

SELECT
ROUND(
  COUNT(DISTINCT iu.airpod_iphone_buyers)::DECIMAL
  / COUNT(DISTINCT transactions.customer_id)::DECIMAL
  * 100, 0)
FROM transactions
LEFT JOIN interested_users AS iu
  ON iu.airpod_iphone_buyers = transactions.customer_id;
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
