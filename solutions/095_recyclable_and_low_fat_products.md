# SQL Everyday \#095

## Recyclable and Low Fat Products

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to find the ids of products that are both low fat and recyclable.

Return the result table in any order. [[Full Description](https://leetcode.com/problems/recyclable-and-low-fat-products/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT 
  product_id 
FROM products 
WHERE low_fats = 'Y'
  AND recyclable = 'Y'
;
```

## Site Solution

```sql
-- LeetCode Solution 
SELECT
  product_id
FROM
  Products
WHERE
  low_fats = 'Y' AND recyclable = 'Y'
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
