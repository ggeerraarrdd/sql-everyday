# SQL Everyday \#125

## Primary Department for Each Employee

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to report all the employees with their primary department. For employees who belong to one department, report their only department.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/primary-department-for-each-employee/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    employee_id
    ,department_id
FROM Employee
GROUP BY employee_id
HAVING COUNT(department_id) = 1
UNION
SELECT
    employee_id
    ,department_id
FROM Employee
WHERE primary_flag = 'Y'
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

`UNION`

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
