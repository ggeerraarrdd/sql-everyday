# SQL Everyday \#064

## Email Table Transformation

Site: DataLemur\
Difficulty per Site: Medium

## Problem

Each Facebook user can designate a personal email address, a business email address, and a recovery email address.

Unfortunately, the table is currently in the wrong format, so you need to transform its structure to show the following columns (see example output): user id, personal email, business email, and recovery email. Sort your answer by user id in ascending order. [[Full Description](https://datalemur.com/questions/email-table-transformation)]

## Submitted Solution

```sql
-- Submitted Solution
WITH personal AS (
  SELECT
    user_id
    ,email AS personal
  FROM users
  WHERE email_type = 'personal'
),
business AS (
  SELECT
    user_id
    ,email AS business
  FROM users
  WHERE email_type = 'business'
),
recovery AS (
  SELECT
    user_id
    ,email AS recovery
  FROM users
  WHERE email_type = 'recovery'
)
SELECT
  DISTINCT users.user_id
  ,personal
  ,business
  ,recovery
FROM users
LEFT JOIN personal ON users.user_id = personal.user_id
LEFT JOIN business ON users.user_id = business.user_id
LEFT JOIN recovery ON users.user_id = recovery.user_id
ORDER BY users.user_id ASC
;
```

## Site Solution

```sql
-- DataLemur Solution 
-- Solution #1: Using CASE Statement
SELECT
  user_id,
  MAX(CASE WHEN email_type = 'personal' THEN email
    ELSE NULL END) AS personal,
  MAX(CASE WHEN email_type = 'business' THEN email
    ELSE NULL END) AS business,
  MAX(CASE WHEN email_type = 'recovery' THEN email
    ELSE NULL END) AS recovery
FROM users
GROUP BY user_id
ORDER BY user_id;

-- Solution #2: Using FILTER
SELECT
  user_id,
  MAX (email) FILTER (WHERE email_type = 'personal') AS personal,
  MAX (email) FILTER (WHERE email_type = 'business') AS business,
  MAX (email) FILTER (WHERE email_type = 'recovery') AS recovery
FROM users
GROUP BY user_id
ORDER BY user_id;
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
