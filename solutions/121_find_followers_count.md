# SQL Everyday \#121

## Find Followers Count

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution that will, for each user, return the number of followers.

Return the result table ordered by `user_id` in ascending order. [[Full Description](https://leetcode.com/problems/find-followers-count/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    user_id
    ,COUNT(follower_id) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id ASC
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- Site solution essentially the same.
```

## Notes

TODO

## NB

TBD

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
