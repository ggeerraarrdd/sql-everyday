# SQL Everyday \#030

## Average Post Hiatus (Part 1)

Site: DataLemur\
Difficulty per Site: Easy

## Problem

Given a table of Facebook posts, for each user who posted at least twice in 2021, write a query to find the number of days between each user’s first post of the year and last post of the year in the year 2021. Output the user and number of the days between each user's first and last post. [[Full Description](https://datalemur.com/questions/sql-average-post-hiatus-1)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
SELECT 
  user_id
  ,MIN(post_date) AS date_min
  ,MAX(post_date) AS date_max
FROM posts
WHERE post_date BETWEEN '01/01/2021' AND '01/01/2022'
GROUP BY user_id
)
SELECT
  user_id
  ,EXTRACT(DAY FROM date_max - date_min) AS days_between
FROM cte
WHERE date_min < date_max
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT 
  user_id, 
    MAX(post_date::DATE) - MIN(post_date::DATE) AS days_between
FROM posts
WHERE DATE_PART('year', post_date::DATE) = 2021 
GROUP BY user_id
HAVING COUNT(post_id)>1;
```

## Notes

TODO

## NB

TBD

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
