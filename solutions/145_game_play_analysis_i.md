# SQL Everyday \#145

## Game Play Analysis I

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to find the first login date for each player.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/game-play-analysis-i/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
    SELECT
    player_id
    ,event_date
    ,ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date ASC) AS rownum
FROM Activity
)
SELECT
    player_id
    ,event_date AS first_login
FROM cte
WHERE rownum = 1
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
