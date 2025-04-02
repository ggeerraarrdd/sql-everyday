# SQL Everyday \#187

## Sales Analysis III

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to report the **products** that were **only** sold in the first quarter of `2019`. That is, between `2019-01-01` and `2019-03-31` inclusive.

Return the resulting table in **any order**. [[Full Description](https://leetcode.com/problems/sales-analysis-iii/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    p.product_id
    ,p.product_name
FROM Sales AS s
JOIN Product AS p ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name
HAVING MIN(sale_date) >= '2019-01-01' AND MAX(sale_date) <= '2019-03-31';
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

`HAVING`

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
