# SQL Everyday \#149

## Sales Person

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to find the names of all the salespersons who did not have any orders related to the company with the name *"RED"*.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/sales-person/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
    SELECT
        *
    FROM Orders AS o
    JOIN Company AS c on o.com_id = c.com_id
),
cte2 AS (
    SELECT
        p.name
        ,COUNT(*) FILTER (WHERE c.name = 'RED') AS ccount
    FROM SalesPerson AS p
    LEFT JOIN cte1 AS c ON p.sales_id = c.sales_id
    GROUP BY p.name
)
SELECT
    name
FROM cte2
WHERE ccount = 0
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
