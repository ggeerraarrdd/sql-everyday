# SQL Everyday \#100

## Replace Employee ID With The Unique Identifier

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to show the *unique ID* of each user, If a user does not have a unique ID replace just show `null`.

Return the result table in *any* order. [[Full Description](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT 
    e2.unique_id
    ,e1.name
FROM Employees as e1
LEFT JOIN EmployeeUNI as e2 ON e1.id = e2.id
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- Site solution essentially the same.
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
