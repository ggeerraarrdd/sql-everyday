# SQL Everyday \#109

## Not Boring Movies

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to report the movies with an odd-numbered ID and a description that is not `"boring"`.

Return the result table ordered by `rating` *in descending order*. [[Full Description](https://leetcode.com/problems/not-boring-movies/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    *
FROM Cinema
WHERE id % 2 <> 0
AND description != 'boring'
ORDER BY rating DESC
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- TODO
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
