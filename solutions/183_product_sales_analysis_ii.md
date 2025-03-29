# SQL Everyday \#183

## Product Sales Analysis II

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution that reports the total quantity sold for every product id.

Return the resulting table in **any order**. [[Full Description](https://leetcode.com/problems/product-sales-analysis-ii/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    product_id
    ,SUM(quantity) AS total_quantity
FROM Sales
GROUP BY product_id
ORDER BY product_id ASC
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- Site solution essentially the same
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
