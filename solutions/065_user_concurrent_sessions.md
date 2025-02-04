# SQL Everyday \#065

## User Concurrent Sessions

Site: DataLemur\
Difficulty per Site: Hard

## Problem

Assume you're given a table containing information about user sessions, including the start and end times of each session. Write a query to retrieve the user session(s) that occur concurrently with the other user sessions.

Output the session ID and the number of concurrent user sessions, sorted in descending order.

Assumptions:

* Concurrent sessions are defined as sessions that overlap with each other. For instance, if session 1 starts before session 2, session 2's start time should fall either before or after session 1's end time.
* Sessions with identical start and end times should not be considered concurrent sessions. [[Full Description](https://datalemur.com/questions/concurrent-user-sessions)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT
    s1.session_id AS session1
    ,s1.start_time AS start_time1
    ,s1.end_time AS end_time1
    ,s2.session_id AS session2
    ,s2.start_time AS start_time2
    ,s2.end_time AS end_time2
    ,CASE 
      WHEN (s1.start_time < s2.start_time AND s2.start_time BETWEEN s1.start_time AND s1.end_time) 
        OR (s2.start_time < s1.start_time AND s1.start_time BETWEEN s2.start_time AND s2.end_time)
      THEN 1 ELSE 0 END AS concurrent
  FROM sessions AS s1
  CROSS JOIN sessions AS s2
  WHERE s1.session_id != s2.session_id
  )
SELECT
  session1
  ,SUM(concurrent) AS concurrent_sessions
FROM cte
GROUP BY session1
HAVING SUM(concurrent) > 0
ORDER BY concurrent_sessions DESC
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT 
  sessions_1.session_id, 
  COUNT(sessions_2.session_id) AS concurrent_sessions 
FROM sessions AS sessions_1 
INNER JOIN sessions AS sessions_2 
  ON sessions_1.session_id != sessions_2.session_id
    AND (sessions_2.start_time BETWEEN sessions_1.start_time AND sessions_1.end_time
    OR sessions_1.start_time BETWEEN sessions_2.start_time AND sessions_2.end_time)
GROUP BY sessions_1.session_id
ORDER BY concurrent_sessions DESC;
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
