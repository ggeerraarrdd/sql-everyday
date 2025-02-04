# SQL Everyday \#105

## Employee Bonus

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to report the name and bonus amount of each employee with a bonus *less than* `1000`.

Return the resulting table in *any order*. [[Full Description](https://leetcode.com/problems/employee-bonus/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    e.name,
    b.bonus
FROM Employee AS e
LEFT JOIN Bonus AS b on e.empID = b.empID
WHERE COALESCE(b.bonus, 0) < 1000
;
```

## Site Solution

```sql
-- LeetCode Solution 
SELECT
    Employee.name, Bonus.bonus
FROM
    Employee
        LEFT JOIN
    Bonus ON Employee.empid = Bonus.empid
WHERE
    bonus < 1000 OR bonus IS NULL
;
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
