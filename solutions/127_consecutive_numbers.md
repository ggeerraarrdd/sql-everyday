# SQL Everyday \#127

## Consecutive Numbers

Site: LeetCode\
Difficulty per Site: Medium

## Problem

Find all numbers that appear at least three times consecutively.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/consecutive-numbers/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
    SELECT
        DISTINCT CASE WHEN l1.num = l2.num AND l2.num = l3.num THEN l1.num ELSE NULL END AS ConsecutiveNums 
    FROM Logs as l1
    JOIN Logs as l2 ON l1.id = l2.id - 1
    JOIN Logs as l3 ON l1.id = l3.id - 2
)
SELECT
    ConsecutiveNums
FROM cte
WHERE ConsecutiveNums IS NOT NULL
;
```

## Site Solution

```sql
-- LeetCode Solution 
SELECT DISTINCT
    l1.Num AS ConsecutiveNums
FROM
    Logs l1,
    Logs l2,
    Logs l3
WHERE
    l1.Id = l2.Id - 1
    AND l2.Id = l3.Id - 1
    AND l1.Num = l2.Num
    AND l2.Num = l3.Num
;
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
