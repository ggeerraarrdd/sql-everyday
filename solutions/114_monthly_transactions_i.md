# SQL Everyday \#114

## Monthly Transactions I

Site: LeetCode\
Difficulty per Site: Medium

## Problem

Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/monthly-transactions-i/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    DATE_FORMAT(trans_date, '%Y-%m') AS month
    ,country
    ,COUNT(trans_date) AS trans_count
    ,SUM(IF(state = 'approved', 1, 0)) AS approved_count
    ,SUM(amount) AS trans_total_amount
    ,SUM(IF(state = 'approved', amount, 0)) AS approved_total_amount
FROM Transactions
GROUP BY month, country
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- None provided
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
