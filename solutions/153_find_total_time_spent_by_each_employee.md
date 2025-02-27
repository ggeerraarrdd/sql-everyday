# SQL Everyday \#153

## Find Total Time Spent by Each Employee

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to calculate the total time *in minutes* spent by each employee on each day at the office. Note that within one day, an employee can enter and leave more than once. The time spent in the office for a single entry is `out_time - in_time`.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/find-total-time-spent-by-each-employee/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    event_day AS day
    ,emp_id
    ,SUM(out_time - in_time) AS total_time
FROM Employees
GROUP BY day, emp_id
ORDER BY day ASC, emp_id ASC
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- TBD
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
