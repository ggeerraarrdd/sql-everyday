# SQL Everyday \#043

## User Shopping Sprees

Site: DataLemur\
Difficulty per Site: Medium

## Problem

In an effort to identify high-value customers, Amazon asked for your help to obtain data about users who go on shopping sprees. A shopping spree occurs when a user makes purchases on 3 or more consecutive days.

List the user IDs who have gone on at least 1 shopping spree in ascending order. [[Full Description](https://datalemur.com/questions/amazon-shopping-spree)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
  SELECT
    *
    ,EXTRACT(DAY FROM COALESCE(LAG(transaction_date, 1) OVER (PARTITION BY user_id ORDER BY transaction_date ASC), transaction_date) - transaction_date) AS lag_date
  FROM transactions
),
cte2 AS (
  SELECT
    *
    ,ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY transaction_date ASC) AS rownum
  FROM cte1
  WHERE lag_date >= -1
)
SELECT
  user_id
FROM cte2
WHERE rownum = 3
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT DISTINCT T1.user_id
FROM transactions AS T1
INNER JOIN transactions AS T2 ON DATE(T2.transaction_date) = DATE(T1.transaction_date) + 1
INNER JOIN transactions AS T3 ON DATE(T3.transaction_date) = DATE(T1.transaction_date) + 2
ORDER BY T1.user_id;
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
