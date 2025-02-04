# SQL Everyday \#017

## Active User Retention

Site: DataLemur\
Difficulty per Site: Hard

## Problem

Assume you're given a table containing information on Facebook user actions. Write a query to obtain number of monthly active users (MAUs) in July 2022, including the month in numerical format "1, 2, 3".

Hint:

* An active user is defined as a user who has performed actions such as 'sign-in', 'like', or 'comment' in both the current month and the previous month. [[Full Description](https://datalemur.com/questions/user-retention)]

## Submitted Solution

```sql
-- Submitted Solution
WITH month_active_current AS (
  SELECT
    user_id
    ,COUNT(DISTINCT event_type) AS distinct_activity_count
  FROM user_actions
  WHERE EXTRACT(MONTH FROM event_date) = month
  GROUP BY user_id
  HAVING COUNT(DISTINCT event_type) > 0
),
month_active_previous AS (
  SELECT
    user_id
    ,COUNT(DISTINCT event_type) AS distinct_activity_count
  FROM user_actions
  WHERE EXTRACT(MONTH FROM event_date + INTERVAL '1 month') = month
  GROUP BY user_id
  HAVING COUNT(DISTINCT event_type) > 0
),
user_active AS (
SELECT
  user_id
FROM month_active_current
INTERSECT
SELECT
  user_id
FROM month_active_previous
)
SELECT
  (SELECT month FROM user_actions LIMIT 1) AS mth
  ,COUNT(DISTINCT user_id) AS month_active_users
FROM user_active
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT 
  EXTRACT(MONTH FROM curr_month.event_date) AS mth, 
  COUNT(DISTINCT curr_month.user_id) AS monthly_active_users 
FROM user_actions AS curr_month
WHERE EXISTS (
  SELECT last_month.user_id 
  FROM user_actions AS last_month
  WHERE last_month.user_id = curr_month.user_id
    AND EXTRACT(MONTH FROM last_month.event_date) =
    EXTRACT(MONTH FROM curr_month.event_date - interval '1 month')
)
  AND EXTRACT(MONTH FROM curr_month.event_date) = 7
  AND EXTRACT(YEAR FROM curr_month.event_date) = 2022
GROUP BY EXTRACT(MONTH FROM curr_month.event_date);
```

## Notes

* My solution is a bit long-winded but I think it shows clearly my step-by-step process.
* Compared to DataLemur's solution, my solution more accurately considers the definition of active user: "who has performed actions such as 'sign-in', 'like', or 'comment' in both the current month and the previous month". So whatever the value is in the `month` column, not 7.

## NB

TBD

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
