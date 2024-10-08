# SQL Everyday \#011

## Histogram of Users and Purchases

Site: DataLemur\
Difficulty per Site: Medium

## Problem

Assume you're given a table on Walmart user transactions. Based on their most recent transaction date, write a query that retrieve the users along with the number of products they bought. Output the user's most recent transaction date, user ID, and the number of products, sorted in chronological order by the transaction date. [[Full Description](https://datalemur.com/questions/histogram-users-purchases)]

## Solution

```sql
-- Submitted Solution
WITH cte1 AS (
  SELECT
    transaction_date::date AS transaction_date
    ,user_id
    ,COUNT(product_id) AS purchase_count
  FROM user_transactions
  GROUP BY transaction_date::date, user_id
),
cte2 AS (
  SELECT
    *
    ,ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY transaction_date DESC) AS row_num
  FROM cte1
)
SELECT
  transaction_date
  ,user_id
  ,purchase_count
FROM cte2
WHERE row_num = 1
ORDER BY transaction_date ASC
;

-- DataLemur Solution
WITH latest_transactions_cte AS (
  SELECT 
    transaction_date, 
    user_id, 
    product_id, 
    RANK() OVER (PARTITION BY user_id ORDER BY transaction_date DESC) AS transaction_rank 
  FROM user_transactions) 
  
SELECT 
  transaction_date, 
  user_id,
  COUNT(product_id) AS purchase_count
FROM latest_transactions_cte
WHERE transaction_rank = 1 
GROUP BY transaction_date, user_id
ORDER BY transaction_date;
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
