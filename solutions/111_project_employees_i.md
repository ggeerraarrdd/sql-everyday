# SQL Everyday \#111

## Project Employees I

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write an SQL query that reports the *average* experience years of all the employees for each project, *rounded to 2 digits*.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/project-employees-i/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    p.project_id
    ,ROUND(AVG(e.experience_years), 2) AS average_years
FROM Project p
JOIN Employee e ON p.employee_id = e.employee_id
GROUP BY p.project_id
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- Site solution essentially the same.
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
