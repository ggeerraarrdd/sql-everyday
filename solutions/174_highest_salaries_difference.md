# SQL Everyday \#174

## Highest Salaries Difference

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to calculate the difference between the *highest* salaries in the *marketing* and *engineering* `department`. Output the absolute difference in salaries. [[Full Description](https://leetcode.com/problems/highest-salaries-difference/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
    SELECT
        MAX(salary) FILTER (WHERE department = 'Engineering') AS engineering_sal
        ,MAX(salary) FILTER (WHERE department = 'Marketing') AS marketing_sal
    FROM Salaries
)
SELECT
    ABS(engineering_sal - marketing_sal) AS salary_difference
FROM
```

## Site Solution

```sql
-- LeetCode Solution 
-- None
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
