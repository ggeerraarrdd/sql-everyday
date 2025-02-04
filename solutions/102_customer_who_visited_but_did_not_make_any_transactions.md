# SQL Everyday \#102

## Customer Who Visited but Did Not Make Any Transactions

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits.

Return the resulting table in *any order*. [[Full Description](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT 
    customer_id, 
    COUNT(*) AS count_no_trans 
FROM Visits AS v 
LEFT JOIN Transactions AS t ON v.visit_id = t.visit_id 
WHERE t.visit_id IS NULL 
GROUP BY customer_id
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- Approach 1: Removing Records Using `NOT IN`/`EXISTS`
SELECT 
  customer_id, 
  COUNT(visit_id) AS count_no_trans 
FROM 
  Visits 
WHERE 
  visit_id NOT IN (
    SELECT 
      visit_id 
    FROM 
      Transactions
  ) 
GROUP BY 
  customer_id

-- Approach 2: Removing Records Using `LEFT JOIN` and `IS NULL`
-- Same as submitted solution.
```

## Notes

TODO

## NB

TBD

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
