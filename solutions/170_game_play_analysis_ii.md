# SQL Everyday \#170

## Game Play Analysis II

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to report the *device* that is first logged in for each player.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/game-play-analysis-ii/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
    SELECT
    player_id
    ,device_id
    ,ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date ASC) AS rownum
FROM Activity
)
SELECT
    player_id
    ,device_id
FROM cte
WHERE rownum = 1
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- Solution 1: Subquery and multi-value use of the IN comparison operator
SELECT
  A1.player_id,
  A1.device_id
FROM
  Activity A1
WHERE
  (A1.player_id, A1.event_date) IN (
    SELECT
      A2.player_id,
      MIN(A2.event_date)
    FROM
      Activity A2
    GROUP BY
      A2.player_id
  );

-- Site 2: Window functions
SELECT DISTINCT
  A.player_id,
  FIRST_VALUE(A.device_id) OVER (
    PARTITION BY
      A.player_id
    ORDER BY
      A.event_date
  ) AS device_id
FROM
  Activity A;
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
