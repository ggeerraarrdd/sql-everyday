# SQL Everyday \#107

## Managers with at Least 5 Direct Reports

Site: LeetCode\
Difficulty per Site: Medium

## Problem

Write a solution to find managers with at least *five direct reports*.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    e1.name
FROM Employee e1
INNER JOIN Employee e2 ON e1.id = e2.managerId
GROUP BY e1.id
HAVING COUNT(e1.id) >= 5
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- TO ADD
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
