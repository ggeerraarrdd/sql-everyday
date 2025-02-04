# SQL Everyday \#126

## Triangle Judgement

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Report for every three line segments whether they can form a triangle.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/triangle-judgement/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    x
    ,y
    ,z
    ,IF(x + y > z AND x + z > y AND y + z > x, 'Yes', 'No') AS triangle
FROM Triangle
; 
```

## Site Solution

```sql
-- LeetCode Solution 
-- Site solution essentially the same.
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
