# SQL Everyday \#061

## First Transaction

Site: DataLemur\
Difficulty per Site: Medium

## Problem

Assume you're given a table containing Etsy user transactions. Write a query that retrieves the customers whose first transaction was valued at $50 or more. Output the total number of users who meet this criteria. [[Full Description](https://datalemur.com/questions/sql-first-transaction)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
SELECT
    *
    ,ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY transaction_date ASC) AS rownum
  FROM user_transactions
)
SELECT
  COUNT(DISTINCT user_id) AS users
FROM cte
WHERE rownum = 1
  AND spend >= 50
;
```

## Site Solution

```sql
-- DataLemur Solution 
WITH ranked_purcases_cte AS (
  SELECT 
    user_id, 
    spend, 
    RANK() OVER (
      PARTITION BY user_id 
      ORDER BY transaction_date ASC) AS ranking 
  FROM user_transactions) 

SELECT COUNT(DISTINCT user_id) AS users
FROM ranked_purcases_cte 
WHERE ranking = 1 
  AND spend >= 50;
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
