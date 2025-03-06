# SQL Everyday \#160

## Employees With Missing Information

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to report the IDs of all the employees with *missing information*. The information of an employee is missing if:

* The employee's *name* is missing, or
* The employee's *salary* is missing.

Return the result table ordered by `employee_id` *in ascending order*. [[Full Description](https://leetcode.com/problems/employees-with-missing-information/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    COALESCE(e.employee_id, s.employee_id) AS employee_id
FROM Employees AS e
FULL JOIN Salaries AS s ON e.employee_id = s.employee_id
WHERE e.name IS NULL
    OR s.salary IS NULL
ORDER BY employee_id ASC
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- Solution #1: Simulate Full Join via Unioning a Left and Right Join
SELECT 
  T.employee_id 
FROM 
  (
    SELECT 
      * 
    FROM 
      Employees 
      LEFT JOIN Salaries USING(employee_id) 
    UNION 
    SELECT 
      * 
    FROM 
      Employees 
      RIGHT JOIN Salaries USING(employee_id)
  ) AS T 
WHERE 
  T.salary IS NULL 
  OR T.name IS NULL 
ORDER BY 
  employee_id;

-- Solution #2: `UNION` with `WHERE ... NOT IN`
SELECT 
  employee_id 
FROM 
  Employees 
WHERE 
  employee_id NOT IN (
    SELECT 
      employee_id 
    FROM 
      Salaries
  ) 
UNION 
SELECT 
  employee_id 
FROM 
  Salaries 
WHERE 
  employee_id NOT IN (
    SELECT 
      employee_id 
    FROM 
      Employees
  ) 
ORDER BY 
  employee_id ASC
```

## Notes

TBD

## NB

FULL JOIN

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
