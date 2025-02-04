# SQL Everyday \#117

## Number of Unique Subjects Taught by Each Teacher

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to calculate the number of unique subjects each teacher teaches in the university.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    teacher_id
    ,COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- Site solution essentially the same.
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
