# SQL Everyday \#115

## Immediate Food Delivery II

Site: LeetCode\
Difficulty per Site: Medium

## Problem

If the customer's preferred delivery date is the same as the order date, then the order is called *immediate*; otherwise, it is called *scheduled*.

The *first order* of a customer is the order with the earliest order date that the customer made. It is guaranteed that a customer has precisely one first order.

Write a solution to find the percentage of immediate orders in the first orders of all customers, *rounded to 2 decimal places*. [[Full Description](https://leetcode.com/problems/immediate-food-delivery-ii/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    ROUND(SUM(IF(order_date = customer_pref_delivery_date, 1, 0)) / COUNT(*) * 100, 2) as immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) IN 
    (
    SELECT
        customer_id
        ,min(order_date)
    FROM Delivery
    GROUP BY customer_id
    )
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- None provided
```

## Notes

TODO

## NB

TBD

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
