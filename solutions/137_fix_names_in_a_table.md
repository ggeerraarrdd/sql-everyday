# SQL Everyday \#137

## Fix Names in a Table

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.

Return the result table ordered by `user_id`. [[Full Description](https://leetcode.com/problems/fix-names-in-a-table/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT 
    user_id
    ,CONCAT(UPPER(SUBSTRING(name, 1, 1)), LOWER(SUBSTRING(name FROM 2))) AS name
FROM Users
ORDER BY user_id
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

`SUBSTRING()`

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
