# SQL Everyday \#130

## Employees Whose Manager Left the Company

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Find the IDs of the employees whose salary is strictly less than `$30000` and whose manager left the company. When a manager leaves the company, their information is deleted from the `Employees` table, but the reports still have their `manager_id` set to the manager that left.

Return the result table ordered by `employee_id`. [[Full Description](https://leetcode.com/problems/employees-whose-manager-left-the-company/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    e1.employee_id AS employee_id
FROM Employees e1
LEFT JOIN Employees e2 ON e1.manager_id = e2.employee_id
WHERE e1.salary < 30000
AND e1.manager_id IS NOT NULL
AND e2.employee_id IS NULL
ORDER BY e1.employee_id ASC
;
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
