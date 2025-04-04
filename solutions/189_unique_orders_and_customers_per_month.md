# SQL Everyday \#189

## Unique Orders and Customers Per Month

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to find the number of **unique orders** and the number of **unique customers** with invoices **> $20** for each **different month**.

Return the resulting table in **any order**. [[Full Description](https://leetcode.com/problems/unique-orders-and-customers-per-month/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    TO_CHAR(order_date, 'YYYY-MM') AS month
    ,COUNT(DISTINCT order_id) AS order_count
    ,COUNT(DISTINCT customer_id) AS customer_count
FROM Orders
WHERE invoice > 20
GROUP BY month
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- None

-- Code Author: Yasin
-- https://leetcode.com/problems/unique-orders-and-customers-per-month/solutions/960078/mysql-solution
-- (modified)
SELECT
    LEFT(order_date, 7) AS month 
    ,COUNT(DISTINCT order_id) AS order_count
    ,COUNT(DISTINCT customer_id) AS customer_count
FROM Orders
WHERE invoice > 20
GROUP BY 1
;
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
