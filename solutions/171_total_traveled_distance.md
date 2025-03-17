# SQL Everyday \#171

## Total Traveled Distance

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to calculate the `distance` traveled by *each user*. If there is a user who hasn't completed any rides, then their distance should be considered as `0`. Output the `user_id`, `name` and total traveled `distance`.

Return the result table ordered by `user_id` in *ascending order*. [[Full Description](https://leetcode.com/problems/total-traveled-distance/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    u.user_id
    ,u.name
    ,COALESCE(SUM(r.distance), 0) AS "traveled distance"
FROM Users AS u
LEFT JOIN Rides AS r ON u.user_id = r.user_id
GROUP BY u.user_id, u.name
ORDER BY u.user_id ASC
;
```

## Site Solution

```sql
-- LeetCode Solution 
SELECT u.user_id, 
       u.name,
       IFNULL(SUM(distance), 0) AS 'traveled distance'
FROM Users AS u
LEFT JOIN Rides AS r
ON u.user_id = r.user_id
GROUP BY user_id, name
ORDER BY user_id 
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
