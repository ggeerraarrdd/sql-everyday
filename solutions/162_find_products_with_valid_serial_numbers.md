# SQL Everyday \#162

## Find Products with Valid Serial Numbers

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to find all products whose description *contains a valid serial number pattern*. A valid serial number follows these rules:

* It starts with the letters *SN* (case-sensitive).
* Followed by exactly `4` digits.
* It must have a hyphen *(-) followed by exactly* `4` digits.

The serial number must be within the description (it may not necessarily start at the beginning).
Return the result table ordered by `product_id` in *ascending* order. [[Full Description](https://leetcode.com/problems/find-products-with-valid-serial-numbers/description/)]

## Submitted Solution

```sql
-- Submitted Solution
-- PostgreSQL
SELECT
    *
FROM products
WHERE description ~ 'SN[0-9]{4}-[0-9]{4}[^0-9]*$'
ORDER BY product_id ASC
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

Regex

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
