# SQL Everyday \#129

## Count Salary Categories

Site: LeetCode\
Difficulty per Site: Medium

## Problem

Write a solution to calculate the number of bank accounts for each salary category. [[Full Description](https://leetcode.com/problems/count-salary-categories/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    "Low Salary" AS category
    ,IFNULL(COUNT(account_id), 0) AS accounts_count
FROM Accounts
WHERE income < 20000
UNION
SELECT
    "Average Salary" AS category
    ,IFNULL(COUNT(account_id), 0) AS accounts_count
FROM Accounts
WHERE income >= 20000 AND income <= 50000
UNION
SELECT
    "High Salary" AS category
    ,IFNULL(COUNT(account_id), 0) AS accounts_count
FROM Accounts
WHERE income > 50000
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

`IFNULL`

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
