# SQL Everyday \#078

## Subject Matter Experts

Site: DataLemur\
Difficulty per Site: Easy

## Problem

You are tasked with identifying Subject Matter Experts (SMEs) at Accenture based on their work experience in specific domains. An employee qualifies as an SME if they meet either of the following criteria:

1. They have 8 or more years of work experience in a single domain.
2. They have 12 or more years of work experience across two different domains.

Write a query to return the employee IDs of all the subject matter experts at Accenture. [[Full Description](https://datalemur.com/questions/subject-matter-experts)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT
    *
    ,CASE WHEN years_of_experience >= 8 THEN 1 ELSE 0 END AS domain_single
    ,SUM(years_of_experience) OVER (PARTITION BY employee_id) AS domain_multi
    ,COUNT(domain) OVER (PARTITION BY employee_id) AS domain_count
  FROM employee_expertise
)
SELECT
  DISTINCT employee_id
FROM cte 
WHERE domain_count <= 2
  AND (domain_single = 1 OR domain_multi >= 12)
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT employee_id
FROM employee_expertise
GROUP BY employee_id
HAVING (SUM(years_of_experience) >= 8 AND COUNT(DISTINCT domain) = 1) 
  OR (SUM(years_of_experience) >=12 AND COUNT(DISTINCT domain) = 2);
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
