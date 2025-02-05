# SQL Everyday \#131

## Exchange Seats

Site: LeetCode\
Difficulty per Site: Medium

## Problem

Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

Return the result table ordered by `id` in *ascending* order. [[Full Description](https://leetcode.com/problems/exchange-seats/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT 
    id
    ,CASE WHEN id % 2 = 0 THEN LAG(student) OVER (ORDER BY id) 
          ELSE COALESCE(LEAD(student) OVER (ORDER BY id), student)
          END AS student
FROM Seat
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

`CASE` w/ `LAG` w/ `COALESCE`

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
