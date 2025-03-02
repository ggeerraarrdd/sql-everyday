# SQL Everyday \#156

## Top Travellers

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to report the distance traveled by each user.

Return the result table ordered by `travelled_distance` in *descending order*, if two or more users traveled the same distance, order them by their `name` in *ascending order*. [[Full Description](https://leetcode.com/problems/top-travellers/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
    SELECT
        user_id
        ,SUM(distance) AS sum_distrance
    FROM rides
    GROUP BY user_id
)
SELECT
    u.name
    ,COALESCE(c.sum_distrance, 0) AS travelled_distance
FROM Users AS u
LEFT JOIN cte AS c ON u.id = c.user_id
ORDER BY travelled_distance DESC, u.name ASC
;
```

## Site Solution

```sql
-- LeetCode Solution 
SELECT 
    u.name, 
    IFNULL(SUM(distance),0) AS travelled_distance
FROM 
    Users u
LEFT JOIN 
    Rides r
ON 
    u.id = r.user_id
GROUP BY 
    u.id
ORDER BY 2 DESC, 1 ASC
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
