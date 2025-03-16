# SQL Everyday \#169

## NPV Queries

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to find the `npv` of each query of the `Queries` table.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/npv-queries/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    q.id
    ,q.year
    ,COALESCE(n.npv, 0) AS npv
FROM Queries AS q
LEFT JOIN NPV AS n ON q.id = n.id
    AND q.year = n.year
;
```

## Site Solution

```sql
-- LeetCode Solution 
SELECT 
  Q.id, 
  Q.year, 
  IFNULL(N.npv, 0) AS npv 
FROM 
  Queries Q 
  LEFT JOIN NPV N ON Q.id = N.id 
  AND Q.year = N.year;
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
