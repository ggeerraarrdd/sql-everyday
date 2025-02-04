# SQL Everyday \#053

## Same Week Purchases

Site: DataLemur\
Difficulty per Site: Hard

## Problem

You are given the two tables containing information on Etsy’s user signups and purchases. Write a query to obtain the percentage of users who signed up and made a purchase within 7 days of signing up. The result should be rounded to the nearest 2 decimal places. [[Full Description](https://datalemur.com/questions/same-week-purchases)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT
    s.user_id
    ,EXTRACT(DAY FROM purchase_date - signup_date) AS diff
    ,ROW_NUMBER() OVER (PARTITION BY signup_date ORDER BY purchase_date ASC) AS rownum
  FROM signups AS s 
  LEFT JOIN user_purchases AS p ON s.user_id = p.user_id
)
SELECT
  ROUND(100.0 * COUNT(user_id) FILTER (WHERE rownum = 1 AND (diff <= 7 OR diff IS NULL)) / COUNT(DISTINCT user_id), 2) AS same_week_purchases_pct
FROM cte 
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT ROUND(
  100.0 * 
    COUNT(DISTINCT purchases.user_id) / 
    COUNT(DISTINCT signups.user_id), 2) AS same_week_purchases_pct
FROM signups
LEFT JOIN user_purchases AS purchases
  ON signups.user_id = purchases.user_id
WHERE purchases.purchase_date IS NULL
  OR (purchases.purchase_date BETWEEN signups.signup_date 
  AND (signups.signup_date + '7 days'::INTERVAL));
```

## Notes

TODO

## NB

TBD

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
