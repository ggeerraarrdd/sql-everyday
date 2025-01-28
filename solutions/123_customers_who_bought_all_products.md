# SQL Everyday \#123

## Customers Who Bought All Products

Site: LeetCode\
Difficulty per Site: Medium

## Problem

Write a solution to report the customer ids from the `Customer` table that bought all the products in the `Product` table.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/customers-who-bought-all-products/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(product_key) FROM Product)
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
