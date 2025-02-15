# SQL Everyday \#141

## List the Products Ordered in a Period

Site: DataLemur\
Difficulty per Site: Easy

## Problem

Write a solution to get the names of products that have at least `100` units ordered in *February 2020* and their amount.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/list-the-products-ordered-in-a-period/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    p.product_name
    ,SUM(unit) AS unit
FROM Products p
JOIN Orders o ON p.product_id = o.product_id
WHERE EXTRACT(YEAR FROM o.order_date) = '2020' 
    AND EXTRACT(MONTH FROM o.order_date) = '02'
GROUP BY product_name
HAVING unit >= 100
ORDER BY product_name ASC
;
```

## Site Solution

```sql
-- DataLemur Solution 
-- None
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
