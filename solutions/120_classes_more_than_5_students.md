# SQL Everyday \#120

## Classes More Than 5 Students

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to find all the classes that have *at least five students*.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/classes-more-than-5-students/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    class
FROM Courses
GROUP BY class
HAVING COUNT(*) >= 5
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
