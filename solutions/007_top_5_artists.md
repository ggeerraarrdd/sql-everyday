# SQL Everyday \#007

## Top 5 Artists

Site: DataLemur\
Difficulty per Site: Medium

## Problem

Write a query to find the top 5 artists whose songs appear most frequently in the Top 10 of the global_song_rank table. Display the top 5 artist names in ascending order, along with their song appearance ranking. If two or more artists have the same number of song appearances, they should be assigned the same ranking, and the rank numbers should be continuous (i.e. 1, 2, 2, 3, 4, 5). [[Full Description](https://datalemur.com/questions/top-fans-rank)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT 
    a.artist_name
    ,DENSE_RANK() OVER (ORDER BY COUNT(s.song_id) DESC) AS artist_rank
  FROM artists AS a
  JOIN songs AS s ON a.artist_id = s.artist_id
  JOIN global_song_rank AS r ON s.song_id = r.song_id
  WHERE r.rank <= 10
  GROUP BY a.artist_name
)
SELECT
  artist_name
  ,artist_rank
FROM cte
WHERE artist_rank <= 5
;
```

## Site Solution

```sql
-- TBD
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
