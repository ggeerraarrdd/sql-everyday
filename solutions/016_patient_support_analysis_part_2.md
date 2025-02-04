# SQL Everyday \#016

## Patient Support Analysis (Part 2)

Site: DataLemur\
Difficulty per Site: Medium

## Problem

UnitedHealth Group (UHG) has a program called Advocate4Me, which allows policy holders (or, members) to call an advocate and receive support for their health care needs – whether that's claims and benefits support, drug coverage, pre- and post-authorisation, medical records, emergency assistance, or member portal services.

Calls to the Advocate4Me call centre are classified into various categories, but some calls cannot be neatly categorised. These uncategorised calls are labeled as “n/a”, or are left empty when the support agent does not enter anything into the call category field.

Write a query to calculate the percentage of calls that cannot be categorised. Round your answer to 1 decimal place. For example, 45.0, 48.5, 57.7. [[Full Description](https://datalemur.com/questions/uncategorized-calls-percentage)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT 
    COUNT(case_id) AS call_total
    ,COUNT(call_category) FILTER (WHERE call_category = 'n/a') AS call_uncategorized
    ,COUNT(call_category) FILTER (WHERE call_category IS NOT NULL) AS call_not_null
  FROM callers 
)
SELECT
  ROUND((call_uncategorized::decimal + (call_total - call_not_null)) / call_total * 100, 1) AS uncategorised_call_pct
FROM cte
;
```

## Site Solution

```sql
-- DataLemur Solution 
WITH uncategorised_callers AS (
  SELECT COUNT(case_id) AS uncategorised_calls
  FROM callers
  WHERE call_category IS NULL
    OR call_category = 'n/a'
)

SELECT 
  ROUND(100.0 * uncategorised_calls / (SELECT COUNT(*) FROM callers), 1) AS uncategorised_call_pct
FROM uncategorised_callers;
```

## Notes

* My approach was to get all the values in the CTE necessary for the calculations in the main `SELECT` statement. DataLemur's solution included a nested query in its main `SELECT` statement to get one of those values.

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
