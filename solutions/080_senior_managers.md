# SQL Everyday \#080

## Senior Managers

Site: DataLemur\
Difficulty per Site: Hard

## Problem

Assume we have a table of Google employees with their corresponding managers.

A manager is an employee with a direct report. A senior manager is an employee who manages at least one manager, but none of their direct reports is senior managers themselves. Write a query to find the senior managers and their direct reports.

Output the senior manager's name and the count of their direct reports. The senior manager with the most direct reports should be the first result. [[Full Description](https://datalemur.com/questions/senior-managers-reportees)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
SELECT
  e1.emp_id
  ,e1.manager_id AS manager
  ,e2.manager_id AS senior_manager
  ,e2.manager_name
FROM employees AS e1
JOIN employees AS e2 ON e1.manager_id = e2.emp_id
JOIN employees AS e3 ON e2.manager_id = e3.emp_id
)
SELECT
  manager_name
  ,COUNT(DISTINCT manager) AS direct_reportees
FROM cte
GROUP BY manager_name
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT 
  managers.manager_name,
  COUNT(DISTINCT managers.emp_id) AS direct_reportees
FROM employees
JOIN employees AS managers
  ON employees.manager_id = managers.emp_id
JOIN employees AS senior_managers
  ON managers.manager_id = senior_managers.emp_id
GROUP BY managers.manager_name
ORDER BY direct_reportees DESC;
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
