# SQL Everyday \#028

## Spotify Streaming History

Site: DataLemur\
Difficulty per Site: Medium

## Problem

You're given two tables containing data on Spotify users' streaming activity: `songs_history` which has historical streaming data, and `songs_weekly` which has data from the current week.

Write a query that outputs the user ID, song ID, and cumulative count of song plays up to August 4th, 2022, sorted in descending order.

Assume that there may be new users or songs in the `songs_weekly` table that are not present in the `songs_history` table. [[Full Description](https://datalemur.com/questions/spotify-streaming-history)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT
    user_id
    ,song_id
    ,COUNT(*) AS week_count_current
  FROM songs_weekly
  WHERE listen_time < '2022-08-05'
  GROUP BY user_id, song_id
)
SELECT
  COALESCE(sh.user_id, cte.user_id) AS user_id
  ,COALESCE(sh.song_id, cte.song_id) AS song_id
  ,COALESCE(sh.song_plays, 0) + COALESCE(cte.week_count_current, 0) AS song_plays
FROM songs_history AS sh
FULL JOIN cte ON sh.user_id = cte.user_id AND sh.song_id = cte.song_id
ORDER BY song_plays DESC
;
```

## Site Solution

```sql
-- DataLemur Solution 
WITH history AS (
  SELECT 
    user_id, 
    song_id, 
    song_plays
  FROM songs_history

  UNION ALL

  SELECT 
    user_id, 
    song_id, 
    COUNT(song_id) AS song_plays
  FROM songs_weekly
  WHERE listen_time <= '08/04/2022 23:59:59'
  GROUP BY user_id, song_id
)

SELECT 
  user_id, 
  song_id, 
  SUM(song_plays) AS song_count
FROM history
GROUP BY 
  user_id, 
  song_id
ORDER BY song_count DESC;
```

## Notes

TODO

## NB

TBD

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
