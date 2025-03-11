# SQL Everyday \#165

## Daily Hospital Admissions and Discharges Report

Site: Codewars\
Difficulty per Site: Medium

## Problem

Write a SQL query to generate a daily report that includes the number of admissions, the number of discharges, the net change in patient count for each day, and the cumulative net change over time. [[Full Description](https://www.codewars.com/kata/66b09bedf5ca866d7ffafc8f)]

## Submitted Solution

```sql
-- Submitted Solution
WITH joins AS (
  SELECT
    TO_CHAR(join_date, 'YYYY-MM-DD') AS j_date
    ,COUNT(entry_id) AS joins
  FROM admissions
  GROUP BY j_date
),
exits AS (
  SELECT
    TO_CHAR(exit_date, 'YYYY-MM-DD') AS e_date
    ,COUNT(entry_id) AS exits
  FROM exits
  GROUP BY e_date
),
net AS (
  SELECT
    COALESCE(j_date, e_date) AS "date"
    ,COALESCE(joins, 0) AS joins
    ,COALESCE(exits, 0) AS exits
    ,CAST(COALESCE(joins, 0) - COALESCE(exits, 0) AS INT) AS net
  FROM joins AS j
  FULL JOIN exits AS e ON j.j_date = e.e_date
)
SELECT
  *
  ,SUM(net) OVER(ORDER BY "date" ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_net
FROM net
;
```

## Site Solution

```sql
-- Codewars Solution 
-- TBD
```

## Notes

TBD

## NB

`TO_CHAR()`

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
