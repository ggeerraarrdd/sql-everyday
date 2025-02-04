# SQL Everyday \#002

## User's Third Transaction

Site: DataLemur\
Difficulty per Site: Medium

## Problem

Write a query to obtain the third transaction of every user. Output the user id, spend and transaction date. [[Full Description](https://datalemur.com/questions/sql-third-transaction)]

## Submitted Solution

```sql
WITH cte AS (
SELECT
  user_id
  ,spend
  ,transaction_date
  ,RANK() OVER (PARTITION BY user_id ORDER BY transaction_date ASC) AS transaction
FROM transactions
)
SELECT
  user_id
  ,spend
  ,transaction_date
FROM cte
WHERE transaction = 3
;
```

## Site Solution

```sql
-- TBD
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
