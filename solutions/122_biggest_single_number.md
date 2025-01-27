# SQL Everyday \#122

## Biggest Single Number

Site: LeetCode\
Difficulty per Site: Easy

## Problem

A *single number* is a number that appeared only once in the `MyNumbers` table.

Find the largest *single number*. If there is no *single number*, report `null`. [[Full Description](https://leetcode.com/problems/biggest-single-number/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    MAX(num) AS num
FROM (
    SELECT
        num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
    ORDER BY num DESC
    ) AS n
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- Site solution essentially the same.
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
