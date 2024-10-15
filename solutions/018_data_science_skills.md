# SQL Everyday \#018

## Data Science Skills

Site: DataLemur\
Difficulty per Site: Easy

## Problem

Given a table of candidates and their skills, you're tasked with finding the candidates best suited for an open Data Science job. You want to find candidates who are proficient in Python, Tableau, and PostgreSQL.

Write a query to list the candidates who possess all of the required skills for the job. Sort the output by candidate ID in ascending order. [[Full Description](https://datalemur.com/questions/matching-skills)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT
    candidate_id
    ,STRING_AGG(LOWER(skill), ' , ') AS skills
  FROM candidates
  GROUP BY candidate_id
)
SELECT
  candidate_id
FROM cte 
WHERE skills LIKE '%python%'
AND skills LIKE '%tableau%'
AND skills LIKE '%postgresql%'
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT candidate_id
FROM candidates
WHERE skill IN ('Python', 'Tableau', 'PostgreSQL')
GROUP BY candidate_id
HAVING COUNT(skill) = 3
ORDER BY candidate_id;
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
