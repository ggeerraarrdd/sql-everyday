# SQL Everyday \#077

## Reactivated Users

Site: DataLemur\
Difficulty per Site: Hard

## Problem

Imagine you're provided with a table containing information about user logins on Facebook in 2022. Write a query that determines the number of reactivated users for a given month. Reactivated users are those who were inactive the previous month but logged in during the current month.

Output the month in numerical format along with the count of reactivated users. [[Full Description](https://datalemur.com/questions/reactivated-users)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT
    *
    ,EXTRACT(YEAR FROM login_date) AS login_year
    ,EXTRACT(MONTH FROM login_date) AS login_month
    ,EXTRACT(YEAR FROM login_date - INTERVAL '1 month') AS login_year_prev
    ,EXTRACT(MONTH FROM login_date - INTERVAL '1 month') AS login_month_prev
  FROM user_logins
)
SELECT
  c1.login_month AS mth
  ,COUNT(DISTINCT c1.user_id) AS reactivated_users
FROM cte AS c1
LEFT JOIN cte AS c2 ON c1.user_id = c2.user_id
  AND c1.login_year_prev = c2.login_year
  AND c1.login_month_prev = c2.login_month
WHERE c2.user_id IS NULL
GROUP BY mth
ORDER BY mth
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT 
  EXTRACT(MONTH FROM curr_month.login_date) AS mth, 
  COUNT(DISTINCT curr_month.user_id) AS reactivated_users
FROM user_logins AS curr_month 
WHERE NOT EXISTS (
  SELECT * 
  FROM user_logins AS last_month 
  WHERE curr_month.user_id = last_month.user_id 
    AND EXTRACT(MONTH FROM last_month.login_date) = 
      EXTRACT(MONTH FROM curr_month.login_date - '1 month' :: INTERVAL)
) 
GROUP BY EXTRACT(MONTH FROM curr_month.login_date)
ORDER BY mth;
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
