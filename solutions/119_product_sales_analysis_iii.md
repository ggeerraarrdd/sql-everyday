# SQL Everyday \#119

## Product Sales Analysis III

Site: LeetCode\
Difficulty per Site: Medium

## Problem

Write a solution to select the `product id`, `year`, `quantity`, and `price` for the `first year` of every product sold.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/product-sales-analysis-iii/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    product_id
    ,year as first_year
    ,quantity
    ,price
FROM Sales
WHERE (product_id, year) IN (
    SELECT 
        product_id
        ,MIN(year) as year
    FROM Sales
    GROUP BY product_id
)
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
