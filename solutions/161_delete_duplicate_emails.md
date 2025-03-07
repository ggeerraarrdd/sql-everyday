# SQL Everyday \#161

## Delete Duplicate Emails

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to *delete* all duplicate emails, keeping only one unique email with the smallest `id`. [[Full Description](https://leetcode.com/problems/delete-duplicate-emails/description/)]

## Submitted Solution

```sql
-- Submitted Solution
DELETE FROM Person 
WHERE id NOT IN (
    SELECT MIN(id) 
    FROM Person 
    GROUP BY email
    )
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
