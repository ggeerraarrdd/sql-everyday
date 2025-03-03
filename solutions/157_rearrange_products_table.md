# SQL Everyday \#157

## Rearrange Products Table

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to rearrange the `Products` table so that each row has `(product_id, store, price)`. If a product is not available in a store, do not include a row with that `product_id` and `store` combination in the result table.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/rearrange-products-table/description/)]

## Submitted Solution

```sql
-- Submitted Solution
-- Write your PostgreSQL query statement below
SELECT
    product_id
    ,'store1' AS store
    ,store1 AS price
FROM Products
WHERE store1 IS NOT NULL
UNION ALL
SELECT
    product_id
    ,'store2' AS store
    ,store2 AS price
FROM Products
WHERE store2 IS NOT NULL
UNION ALL
SELECT
    product_id
    ,'store3' AS store
    ,store3 AS price
FROM Products
WHERE store3 IS NOT NULL
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
