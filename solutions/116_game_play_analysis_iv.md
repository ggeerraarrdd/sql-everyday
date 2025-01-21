# SQL Everyday \#116

## Game Play Analysis IV

Site: LeetCode\
Difficulty per Site: Medium

## Problem

Write a solution to report the *fraction* of players that logged in again on the day after the day they first logged in, *rounded to 2 decimal places*. In other words, you need to count the number of players that logged in for at least two consecutive days starting from their first login date, then divide that number by the total number of players. [[Full Description](https://leetcode.com/problems/game-play-analysis-iv/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS
    (
    SELECT
        player_id
        ,DATE(MIN(event_date) + INTERVAL 1 DAY) AS second_day
    FROM Activity
    GROUP BY player_id
    )
SELECT
    ROUND(COUNT(*) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM Activity a
JOIN cte ON a.player_id = cte.player_id AND a.event_date = cte.second_day
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- Approach 1: Subqueries and multi-value use of the IN comparison operator
SELECT
  ROUND(
    COUNT(A1.player_id)
    / (SELECT COUNT(DISTINCT A3.player_id) FROM Activity A3)
  , 2) AS fraction
FROM
  Activity A1
WHERE
  (A1.player_id, DATE_SUB(A1.event_date, INTERVAL 1 DAY)) IN (
    SELECT
      A2.player_id,
      MIN(A2.event_date)
    FROM
      Activity A2
    GROUP BY
      A2.player_id
  );
  
-- Approach 2: CTEs and INNER JOIN
WITH first_logins AS (
  SELECT
    A.player_id,
    MIN(A.event_date) AS first_login
  FROM
    Activity A
  GROUP BY
    A.player_id
), consec_logins AS (
  SELECT
    COUNT(A.player_id) AS num_logins
  FROM
    first_logins F
    INNER JOIN Activity A ON F.player_id = A.player_id
    AND F.first_login = DATE_SUB(A.event_date, INTERVAL 1 DAY)
)
SELECT
  ROUND(
    (SELECT C.num_logins FROM consec_logins C)
    / (SELECT COUNT(F.player_id) FROM first_logins F)
  , 2) AS fraction;
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
