# SQL Everyday \#158

## Calculate Special Bonus

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to calculate the bonus of each employee. The bonus of an employee is `100%` of their salary if the ID of the employee is *an odd number* and *the employee's name does not start with the character* `'M'`. The bonus of an employee is `0` otherwise.

Return the result table ordered by `employee_id`. [[Full Description](https://leetcode.com/problems/calculate-special-bonus/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    employee_id
    ,CASE WHEN name NOT LIKE 'M%' AND employee_id % 2 != 0 THEN salary ELSE 0 END AS bonus
FROM Employees
ORDER BY employee_id ASC
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
