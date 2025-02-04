# SQL Everyday \#004

## Sending vs. Opening Snaps

Site: DataLemur\
Difficulty per Site: Medium

## Problem

Write a query to obtain a breakdown of the time spent sending vs. opening snaps as a percentage of total time spent on these activities grouped by age group. Round the percentage to 2 decimal places in the output. [[Full Description](https://datalemur.com/questions/time-spent-snaps)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
  SELECT 
    age_bucket
    ,SUM(a.time_spent) AS time_all_total
  FROM activities AS a 
  JOIN age_breakdown AS ab ON a.user_id = ab.user_id
  WHERE activity_type IN ('send', 'open')
  GROUP BY age_bucket
),
cte2 AS (
  SELECT 
    ab.age_bucket
    ,a.activity_type
    ,SUM(time_spent) AS time_activity_total
  FROM activities AS a 
  JOIN age_breakdown AS ab ON a.user_id = ab.user_id
  WHERE activity_type IN ('send', 'open')
  GROUP BY ab.age_bucket, a.activity_type
),
cte3 AS (
  SELECT 
    cte2.age_bucket
    ,cte2.activity_type
    ,ROUND(cte2.time_activity_total / cte1.time_all_total * 100, 2) AS time_all_perc
  FROM cte1
  JOIN cte2 ON cte1.age_bucket = cte2.age_bucket
),
cte4 AS (
  SELECT 
    age_bucket
    ,time_all_perc AS send_perc
  FROM cte3
  WHERE activity_type = 'send'
),
cte5 AS (
  SELECT 
    age_bucket
    ,time_all_perc AS open_perc
  FROM cte3
  WHERE activity_type = 'open'
)
SELECT 
  cte4.age_bucket
  ,cte4.send_perc
  ,cte5.open_perc
FROM cte4
JOIN cte5 ON cte4.age_bucket = cte5.age_bucket
;
```

## Site Solution

```sql
-- DataLemur Solution
SELECT 
  age.age_bucket, 
  ROUND(100.0 * 
    SUM(activities.time_spent) FILTER (WHERE activities.activity_type = 'send')/
    SUM(activities.time_spent),2) AS send_perc, 
  ROUND(100.0 * 
    SUM(activities.time_spent) FILTER (WHERE activities.activity_type = 'open')/
    SUM(activities.time_spent),2) AS open_perc
FROM activities
INNER JOIN age_breakdown AS age 
  ON activities.user_id = age.user_id 
WHERE activities.activity_type IN ('send', 'open') 
GROUP BY age.age_bucket;
```

## Notes

* One of the reasons I started this personal SQL Everyday chellenge is to learn SQL concepts and techniques new to me. This problem delivered with [`FILTER()`](https://www.postgresql.org/docs/current/sql-expressions.html#SYNTAX-AGGREGATES) from DataLemur's solutions. The reduction of lines from my query to that solution is remarkable.

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
