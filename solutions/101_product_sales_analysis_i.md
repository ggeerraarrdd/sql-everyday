# SQL Everyday \#101

## Product Sales Analysis I

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to report the `product_name`, `year`, and `price` for each `sale_id` in the `Sales` table.

Return the resulting table in *any order*. [[Full Description](https://leetcode.com/problems/product-sales-analysis-i/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    p.product_name
    ,s.year
    ,s.price
FROM Sales AS s
JOIN Product AS p ON s.product_id = p.product_id
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
