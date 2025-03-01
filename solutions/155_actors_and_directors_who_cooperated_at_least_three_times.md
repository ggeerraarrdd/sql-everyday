# SQL Everyday \#155

## Actors and Directors Who Cooperated At Least Three Times

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to find all the pairs `(actor_id, director_id)` where the actor has cooperated with the director at least three times.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    actor_id
    ,director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(*) >= 3
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- TBD
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
