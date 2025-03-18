# SQL Everyday \#172

## Create a Session Bar Chart

Site: LeetCode\
Difficulty per Site: Easy

## Problem

You want to know how long a user visits your application. You decided to create bins of `"[0-5>"`, `"[5-10>"`, `"[10-15>"`, and `"15 minutes or more"` and count the number of sessions on it.

Write a solution to report the `(bin, total)`.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/create-a-session-bar-chart/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
    SELECT '[0-5>' AS bin FROM Sessions
    UNION
    SELECT '[5-10>' AS bin FROM Sessions
    UNION
    SELECT '[10-15>' AS bin FROM Sessions
    UNION
    SELECT '15 or more' AS bin FROM Sessions
),
cte2 AS (
SELECT
    CASE WHEN (duration/60) < 5 THEN '[0-5>' 
         WHEN (duration/60) < 10 THEN '[5-10>'
         WHEN (duration/60) < 15 THEN '[10-15>' 
         ELSE '15 or more' END AS bin
FROM Sessions
)
SELECT
    c1.bin
    ,COALESCE(COUNT(c2.bin), 0) AS total
FROM cte1 AS c1
LEFT JOIN cte2 AS c2 ON c1.bin = c2.bin
GROUP BY c1.bin
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- None
```

## Notes

This is easy enough with `CASE` and `GROUP BY`. But the not-so easy part is ensuring any missing bin is also counted as 0.

## NB

Histogram bins w/ `UNION`, `CASE`

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
