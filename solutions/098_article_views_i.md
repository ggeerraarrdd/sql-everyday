# SQL Everyday \#098

## Article Views I

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by `id` in ascending order. [[Full Description](https://leetcode.com/problems/article-views-i/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT 
    DISTINCT v1.author_id AS id
FROM Views as v1
JOIN Views as v2 ON v1.author_id = v2.author_id 
WHERE v1.author_id = v2.viewer_id
ORDER BY id ASC
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
