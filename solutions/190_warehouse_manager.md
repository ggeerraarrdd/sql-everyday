# SQL Everyday \#190

## Warehouse Manager

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to report the number of cubic feet of **volume** the inventory occupies in each warehouse.

Return the resulting table in **any order**. [[Full Description](https://leetcode.com/problems/warehouse-manager/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    w.name AS warehouse_name
    ,SUM(w.units * p.Width * p.Length * p.Height) AS volume
FROM Products AS p
JOIN Warehouse AS w ON p.product_id = w.product_id
GROUP BY warehouse_name
;
```

## Site Solution

```sql
-- LeetCode Solution 
SELECT 
    w.name AS warehouse_name, 
    sum(w.units * sub.cubic_ft) AS volume
FROM 
    Warehouse w
LEFT JOIN (
    SELECT 
        p.product_id, 
        p.width * p.length * p.height AS cubic_ft
    FROM Products p
) AS sub
ON w.product_id = sub.product_id
GROUP BY warehouse_name;
```

## Notes

Site solution uses a subquery. But as in the submitted solution, can solved using `JOIN`.

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
