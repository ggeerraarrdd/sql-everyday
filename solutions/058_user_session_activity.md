# SQL Everyday \#058

## User Session Activity

Site: DataLemur\
Difficulty per Site: Medium

## Problem

Assume you are given the table containing Twitter user session activities.

Write a query that ranks users according to their total session durations (in minutes) in descending order for each session type between the start date (2022-01-01) and the end date (2022-02-01).

Output the user ID, session type, and the ranking of the total session duration. [[Full Description](https://datalemur.com/questions/user-session-activity)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT
    user_id
    ,session_type
    ,SUM(duration) AS duration
  FROM sessions
  WHERE start_date BETWEEN '2022-01-01' AND '2022-02-02'
  GROUP BY user_id, session_type
)
SELECT
  user_id
  ,session_type
  ,RANK() OVER (PARTITION BY session_type ORDER BY duration DESC) AS ranking
FROM cte
;
```

## Site Solution

```sql
-- DataLemur Solution 
-- Site solution is essentially the same.
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
