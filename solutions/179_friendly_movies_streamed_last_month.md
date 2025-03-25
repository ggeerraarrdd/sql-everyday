# SQL Everyday \#179

## Friendly Movies Streamed Last Month

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to report the distinct titles of the kid-friendly movies streamed in **June 2020**.

Return the result table in **any order**. [[Full Description](https://leetcode.com/problems/friendly-movies-streamed-last-month/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    DISTINCT c.title
FROM TVProgram AS t
JOIN Content AS c ON t.content_id = c.content_id
WHERE c.Kids_content = 'Y'
    AND c.content_type = 'Movies'
    AND DATE_FORMAT(t.program_date,'%Y-%m') = '2020-06'
;
```

## Site Solution

```sql
-- LeetCode Solution 
SELECT 
    DISTINCT c.title
FROM 
    Content c
JOIN 
    TVProgram p
ON 
    c.content_id = p.content_id
WHERE 
    c.Kids_content = 'Y'
AND 
    c.content_type = 'Movies'
AND MONTH(p.program_date) = 6 AND YEAR(p.program_date) = 2020
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
