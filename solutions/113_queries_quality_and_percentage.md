# SQL Everyday \#113

## Queries Quality and Percentage

Site: LeetCode\
Difficulty per Site: Easy

## Problem

We define query `quality` as:

> The average of the ratio between query rating and its position.

We also define `poor query percentage` as:

The percentage of all queries with rating less than 3.

Write a solution to find each `query_name`, the `quality` and `poor_query_percentage`.

Both `quality` and `poor_query_percentage` should be *rounded to 2 decimal places*.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/queries-quality-and-percentage/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    query_name
    ,ROUND(SUM(rating / position) / COUNT(*), 2) as quality
    ,ROUND(SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) / COUNT(*) * 100, 2) AS poor_query_percentage
FROM Queries
WHERE query_name IS NOT NULL
GROUP BY query_name
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- None provided
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
