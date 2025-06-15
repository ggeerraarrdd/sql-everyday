# SQL Everyday \#195

## Game Play Analysis III

Site: LeetCode\
Difficulty per Site: Medium

## Problem

Write a solution to report for each player and date, how many games played **so far** by the player. That is, the total number of games played by the player until that date. Check the example for clarity.

Return the result table in **any order**. [[Full Description](https://leetcode.com/problems/game-play-analysis-iii/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    player_id
    ,event_date
    ,SUM(games_played) OVER (PARTITION BY player_id ORDER BY event_date ASC) AS games_played_so_far
FROM Activity
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- Non-equi self join
SELECT
  A2.player_id,
  A2.event_date,
  SUM(A1.games_played) AS games_played_so_far
FROM
  Activity A1
  INNER JOIN Activity A2 ON A1.player_id = A2.player_id
  AND A1.event_date <= A2.event_date
GROUP BY
  A2.player_id,
  A2.event_date;
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
