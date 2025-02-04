# SQL Everyday \#097

## Big Countries

Site: LeetCode\
Difficulty per Site: Easy

## Problem

A country is big if:

* it has an area of at least three million (i.e., 3000000 km2), or
* it has a population of at least twenty-five million (i.e., 25000000).

Write a solution to find the name, population, and area of the big countries.

Return the result table in any order. [[Full Description](https://leetcode.com/problems/big-countries/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    name
    ,population
    ,area
FROM World
WHERE area >= 3000000
    OR population >= 25000000
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

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
