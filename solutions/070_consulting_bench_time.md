# SQL Everyday \#070

## Consulting Bench Time

Site: DataLemur\
Difficulty per Site: Medium

## Problem

In consulting, being "on the bench" means you have a gap between two client engagements. Google wants to know how many days of bench time each consultant had in 2021. Assume that each consultant is only staffed to one consulting engagement at a time.

Write a query to pull each employee ID and their total bench time in days during 2021. [[Full Description](https://datalemur.com/questions/consulting-bench-time)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
  s.employee_id
  ,365 - SUM(ce.end_date - ce.start_date) - COUNT(s.job_id) AS bench_days
FROM consulting_engagements AS ce 
JOIN staffing AS s on ce.job_id = s.job_id
WHERE s.is_consultant = 'true'
GROUP BY employee_id
;
```

## Site Solution

```sql
-- DataLemur Solution 
WITH consulting_days AS (
SELECT 
  staffs.employee_id,
  SUM(engagements.end_date - engagements.start_date) AS non_bench_days,
  COUNT(staffs.employee_id) AS inclusive_days
FROM staffing AS staffs
INNER JOIN consulting_engagements AS engagements
  ON staffs.job_id = engagements.job_id
WHERE staffs.is_consultant = 'true'
GROUP BY staffs.employee_id)

SELECT
  employee_id,
  365 - SUM(non_bench_days) - SUM(inclusive_days) AS bench_days
FROM consulting_days
GROUP BY employee_id;
```

## Notes

* Submitted and site solutions do no consider dates outside 2021. To do so, use `CASE WHEN...` to truncate dates to the beginning or end of the year.

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
