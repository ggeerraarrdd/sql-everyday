# SQL Everyday \#132

## Movie Rating

Site: LeetCode\
Difficulty per Site: Medium

## Problem

Write a solution to:

* Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
* Find the movie name with the *highest average* rating in `February 2020`. In case of a tie, return the lexicographically smaller movie name. [[Full Description](https://leetcode.com/problems/movie-rating/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
    SELECT
        mr.user_id
        ,u.name
        ,COUNT(mr.rating) AS count_ratings
    FROM MovieRating AS mr
    JOIN Users u ON mr.user_id = u.user_id
    GROUP BY mr.user_id
    ORDER BY count_ratings DESC, u.name ASC
    LIMIT 1
),
cte2 AS (
    SELECT
        mr.movie_id
        ,mv.title
        ,AVG(mr.rating) AS avg_rating
        ,mr.created_at
    FROM MovieRating AS mr
    JOIN Movies mv ON mr.movie_id = mv.movie_id
    WHERE EXTRACT(YEAR FROM mr.created_at) = 2020 AND EXTRACT(MONTH FROM mr.created_at) = 2
    GROUP BY mr.movie_id
    ORDER BY avg_rating DESC, mv.title ASC
    LIMIT 1
)
SELECT
    name AS results
FROM cte1
UNION ALL
SELECT
    title AS results
FROM cte2
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- None
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
