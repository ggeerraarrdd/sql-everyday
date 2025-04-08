# SQL Everyday \#192

## Find Candidates for Data Scientist Position

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a query to find the **candidates** best suited for a Data Scientist position. The candidate must be proficient in **Python**, **Tableau**, and **PostgreSQL**.

Return the result table ordered by *candidate_id* in **ascending order**. [[Full Description](https://leetcode.com/problems/find-candidates-for-data-scientist-position/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
    SELECT
        candidate_id
        ,STRING_AGG(LOWER(skill), ',') AS skills
    FROM Candidates
    GROUP BY candidate_id
)
SELECT
    candidate_id
FROM cte
WHERE skills LIKE '%python%'
    AND skills LIKE '%tableau%'
    AND skills LIKE '%postgresql%'
ORDER BY candidate_id ASC
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- No site solution provided

-- Code Author: Shubham Tiwari
-- https://leetcode.com/problems/find-candidates-for-data-scientist-position/solutions/4785812/easy-solution
SELECT 
    candidate_id
FROM candidates
WHERE skill IN ('Python','Tableau','PostgreSQL')
GROUP BY 1
HAVING COUNT(skill) = 3
ORDER BY 1 ASC
;
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
