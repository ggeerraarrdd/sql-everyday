# SQL Everyday \#178

## Shortest Distance in a Line

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Find the shortest distance between any two points from the `Point` table. [[Full Description](https://leetcode.com/problems/shortest-distance-in-a-line/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    MIN(ABS(p1.x - p2.x)) AS shortest
FROM Point AS p1
JOIN Point AS p2 ON p1.x != p2.x 
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- Site solution essentially the same
```

## Notes

TBD

## NB

`SELF-JOIN` vs `CROSS JOIN`

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
