# SQL Everyday \#146

## Department Highest Salary

Site: LeetCode\
Difficulty per Site: Medium

## Problem

Write a solution to find employees who have the highest salary in each of the departments.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/department-highest-salary/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
SELECT
    d.name AS Department
    ,e.name AS Employee
    ,salary AS Salary
    ,RANK() OVER (PARTITION BY e.departmentID ORDER BY e.salary DESC) AS rownum
FROM Employee AS e
JOIN Department AS d ON e.departmentID = d.id
)
SELECT
    Department
    ,Employee
    ,Salary
FROM cte
WHERE rownum = 1
ORDER BY Salary DESC
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
