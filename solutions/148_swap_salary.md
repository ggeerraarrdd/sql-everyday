# SQL Everyday \#148

## Swap Salary

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to swap all `'f'` and `'m'` values (i.e., change all `'f'` values to `'m'` and vice versa) with a *single update statement* and no intermediate temporary tables.

Note that you must write a single update statement, *do not* write any select statement for this problem. [[Full Description](https://leetcode.com/problems/swap-salary/description/)]

## Submitted Solution

```sql
-- Submitted Solution
UPDATE Salary 
SET sex = (CASE WHEN sex = 'f' THEN 'm' ELSE 'f' END)
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
