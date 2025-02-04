# SQL Everyday \#081

## LinkedIn Power Creators (Part 1)

Site: DataLemur\
Difficulty per Site: Easy

## Problem

The LinkedIn Creator team is seeking out individuals who have a strong influence on the platform, utilizing their personal profiles as a company or influencer page. To identify such power creators, we can compare the number of followers on their LinkedIn page with the number of followers on the company they work for. If a person's LinkedIn page has more followers than their company, we consider them to be a power creator.

Write a query to retrieve the profile IDs of these LinkedIn power creators ordered in ascending order based on their IDs. [[Full Description](https://datalemur.com/questions/linkedin-power-creators)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
  pp.profile_id
FROM personal_profiles AS pp 
JOIN company_pages AS cp ON pp.employeR_id = cp.company_id
WHERE pp.followers > cp.followers
ORDER BY pp.profile_id ASC
;
```

## Site Solution

```sql
-- DataLemur Solution 
-- Site solution essentially the same.
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
