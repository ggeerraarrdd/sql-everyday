# SQL Everyday \#124

## The Number of Employees Which Report to Each Employee

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to report the ids and the names of all *managers*, the number of employees who report *directly* to them, and the average age of the reports rounded to the nearest integer.

Return the result table ordered by `employee_id`. [[Full Description](https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT 
    e1.employee_id
    ,e1.name
    ,COUNT(e2.employee_id) AS reports_count
    ,ROUND(AVG(e2.age)) AS average_age
FROM Employees e1
JOIN Employees e2 ON e1.employee_id = e2.reports_to
WHERE e2.reports_to IS NOT NULL
GROUP BY e1.employee_id
ORDER BY e1.employee_id
;
```

## Site Solution

```sql
-- LeetCode Solution 
SELECT 
  reports_to AS employee_id, 
  (
    SELECT 
      name 
    FROM 
      employees e1 
    WHERE 
      e.reports_to = e1.employee_id 
  ) AS name, 
  COUNT(reports_to) AS reports_count, 
  ROUND(
    AVG(age)
  ) AS average_age 
FROM 
  employees e 
GROUP BY 
  reports_to 
HAVING 
  reports_count > 0 
ORDER BY 
  employee_id
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
