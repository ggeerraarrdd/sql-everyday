# SQL Everyday \#052

## LinkedIn Power Creators (Part 2)

Site: DataLemur\
Difficulty per Site: Medium

## Problem

The LinkedIn Creator team is looking for power creators who use their personal profile as a company or influencer page. This means that if someone's Linkedin page has more followers than all the company they work for, we can safely assume that person is a Power Creator. Keep in mind that if a person works at multiple companies, we should take into account the company with the most followers.

Write a query to return the IDs of these LinkedIn power creators in ascending order. [[Full Description](https://datalemur.com/questions/linkedin-power-creators-part2)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT
    pp.profile_id
    ,pp.name
    ,pp.followers AS personal_followers
    ,cp.company_id
    ,cp.followers AS company_followers
    ,ROW_NUMBER() OVER (PARTITION BY pp.profile_id ORDER BY cp.followers DESC) AS rownum
    ,CASE WHEN pp.followers >= cp.followers THEN 1 ELSE 0 END AS power_key
  FROM employee_company AS ec 
  JOIN company_pages AS cp ON ec.company_id = cp.company_id
  JOIN personal_profiles AS pp on ec.personal_profile_id = pp.profile_id
)
SELECT
  profile_id
FROM cte
WHERE rownum = 1
  AND power_key = 1
;
```

## Site Solution

```sql
-- DataLemur Solution 
WITH popular_companies 
AS (
  SELECT
    employees.personal_profile_id,
    MAX(pages.followers) AS highest_followers
  FROM employee_company AS employees 
  LEFT JOIN company_pages AS pages
    ON employees.company_id = pages.company_id  
  GROUP BY employees.personal_profile_id)

SELECT profiles.profile_id
FROM popular_companies AS companies
LEFT JOIN personal_profiles AS profiles
  ON companies.personal_profile_id = profiles.profile_id
WHERE profiles.followers > companies.highest_followers
ORDER BY profiles.profile_id;
```

## Notes

TODO

## NB

TBD

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
