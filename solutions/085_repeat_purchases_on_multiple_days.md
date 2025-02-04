# SQL Everyday \#085

## Repeat Purchases on Multiple Days

Site: DataLemur\
Difficulty per Site: Medium

## Problem

Assume you are given the table below containing information on user purchases. Write a query to obtain the number of users who purchased the same product on two or more different days. Output the number of unique users. [[Full Description](https://datalemur.com/questions/sql-repeat-purchases)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT
    user_id
    ,RANK() OVER (PARTITION BY user_id, product_id ORDER BY DATE_TRUNC('day', purchase_date) ASC) AS rownum
  FROM purchases
)
SELECT
  COUNT(user_id) AS repeat_purchasers
FROM cte
WHERE rownum = 2
;
```

## Site Solution

```sql
-- DataLemur Solution 
WITH repeat_purchases AS (
SELECT DISTINCT user_id AS users
FROM purchases
GROUP BY user_id, product_id
HAVING COUNT(DISTINCT purchase_date::DATE) > 1
)

SELECT COUNT(DISTINCT users) AS repeated_purchasers
FROM repeat_purchases;
```

## Notes

TODO

## NB

`DATE_TRUNC` vs `::DATE`

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
