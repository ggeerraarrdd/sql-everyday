# SQL Everyday \#186

## Sales Analysis II

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to report the **buyers** who have bought *S8* but not *iPhone*. Note that *S8* and *iPhone* are products presented in the `Product` table.

Return the resulting table in **any order**. [[Full Description](https://leetcode.com/problems/sales-analysis-ii/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
    SELECT
        s.buyer_id
        ,STRING_AGG(p.product_name, ',') AS products
    FROM Sales AS s
    JOIN Product AS p ON s.product_id = p.product_id
    GROUP BY s.buyer_id
)
SELECT
    buyer_id
FROM cte
WHERE products LIKE '%S8%'
    AND products NOT LIKE '%iPhone%'
;
```

## Site Solution

```sql
-- LeetCode Solution 
SELECT DISTINCT s.buyer_id
FROM Sales s
JOIN Product p
ON s.product_id = p.product_id
GROUP BY s.buyer_id
HAVING GROUP_CONCAT(p.product_name) LIKE '%S8%'
AND GROUP_CONCAT(p.product_name) NOT LIKE '%iPhone%'
```

## Notes

TBD

## NB

`STRING_AGG` vs `GROUP_CONCAT`

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
