# SQL Everyday \#147

## Customer Placing the Largest Number of Orders

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to find the `customer_number` for the customer who has placed *the largest number of orders*.

The test cases are generated so that *exactly one customer* will have placed more orders than any other customer. [[Full Description](https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(order_number) DESC
LIMIT 1
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

`ORDER BY` w/ Aggregate Function

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
