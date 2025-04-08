# SQL Everyday \#191

## The Number of Rich Customers

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to report the number of customers who had **at least one** bill with an amount **strictly greater** than `500`.

Return the resulting table in **any order**. [[Full Description](https://leetcode.com/problems/the-number-of-rich-customers/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    COUNT(DISTINCT customer_id) AS rich_count
FROM Store
WHERE amount > 500
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- Site solution essentially the same.
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
