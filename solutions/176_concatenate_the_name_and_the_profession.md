# SQL Everyday \#176

## Concatenate the Name and the Profession

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to report each person's name followed by the first letter of their profession enclosed in parentheses.

Return the result table **ordered** by `person_id` in **descending order**. [[Full Description](https://leetcode.com/problems/concatenate-the-name-and-the-profession/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    person_id
    ,CONCAT(name, '(', SUBSTRING(profession, 1, 1), ')') AS name
FROM Person
ORDER BY person_id DESC
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- Code Author: Mathieu Soysal
-- https://leetcode.com/problems/concatenate-the-name-and-the-profession/solutions/5003721/simple-postgresql-solution-with-concat-and-left
SELECT person_id,
    CONCAT(name, '(' , LEFT(profession, 1), ')') AS name
FROM Person
ORDER BY person_id DESC;
```

## Notes

TBD

## NB

`SUBSTRING` vs `LEFT`

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
