# SQL Everyday \#083

## Event Friends Recommendation

Site: DataLemur\
Difficulty per Site: Hard

## Problem

Facebook wants to recommend new friends to people who show interest in attending 2 or more of the same private events. [[Full Description](https://datalemur.com/questions/event-friends-rec)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
  SELECT
    CASE WHEN e1.user_id < e2.user_id THEN e1.user_id ELSE e2.user_id END AS u1
    ,CASE WHEN e1.user_id < e2.user_id THEN e2.user_id ELSE e1.user_id END AS u2
  FROM event_rsvp AS e1
  JOIN event_rsvp AS e2 ON e1.event_id = e2.event_id
  WHERE e1.event_type = 'private'
    AND e1.attendance_status IN ('going', 'maybe')
    AND e2.event_type = 'private'
    AND e2.attendance_status IN ('going', 'maybe')
    AND e1.user_id != e2.user_id
),
cte2 AS (
  SELECT
    u1
    ,u2
    ,ROW_NUMBER() OVER (PARTITION BY u1, u2) AS rownum
  FROM cte1
),
cte3 AS (
  SELECT
    c.u1 AS user_a_id
    ,c.u2 AS user_b_id
  FROM cte2 AS c
  JOIN friendship_status AS f ON c.u1 = f.user_a_id
  WHERE rownum = 1
    AND c.u2 = f.user_b_id
    AND f.status = 'not_friends'
)
SELECT
  user_a_id
  ,user_b_id
FROM cte3
UNION 
SELECT
  user_b_id
  ,user_a_id
FROM cte3
;
```

## Site Solution

```sql
-- DataLemur Solution 
WITH private_events AS (
SELECT user_id, event_id
FROM event_rsvp
WHERE attendance_status IN ('going', 'maybe')
  AND event_type = 'private'
)

SELECT 
  friends.user_a_id, 
  friends.user_b_id
FROM private_events AS events_1
INNER JOIN private_events AS events_2
  ON events_1.user_id != events_2.user_id
  AND events_1.event_id = events_2.event_id
INNER JOIN friendship_status AS friends
  ON events_1.user_id = friends.user_a_id
  AND events_2.user_id = friends.user_b_id
WHERE friends.status = 'not_friends'
GROUP BY friends.user_a_id, friends.user_b_id
HAVING COUNT(*) >= 2;
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
