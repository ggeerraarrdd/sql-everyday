# SQL Everyday \#138

## Patients With a Condition

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to find the patient_id, patient_name, and conditions of the patients who have Type I Diabetes. Type I Diabetes always starts with `DIAB1` prefix.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/patients-with-a-condition/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    *
FROM Patients
WHERE (conditions LIKE "DIAB1%") OR (conditions LIKE "% DIAB1%")
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



Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)

