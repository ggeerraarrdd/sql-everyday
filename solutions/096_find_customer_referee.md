# SQL Everyday \#096

## Find Customer Referee

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Find the names of the customer that are not referred by the customer with `id = 2`.

Return the result table in any order. [[Full Description](https://leetcode.com/problems/find-customer-referee/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT 
  name
FROM Customer
WHERE COALESCE(referee_id, 0) NOT IN (2)
;
```

## Site Solution

```sql
-- LeetCode Solution 
SELECT name FROM customer WHERE referee_id <> 2 OR referee_id IS NULL;
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
