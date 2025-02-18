# SQL Everyday \#144

## Customers Who Never Order

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to find all customers who never order anything.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/customers-who-never-order/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    name AS Customers
FROM Customers AS c
LEFT JOIN Orders AS o ON c.id = o.customerID
WHERE o.customerID IS NULL
ORDER BY Customers ASC
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
