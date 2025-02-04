# SQL Everyday \#069

## Patient Support Analysis (Part 1)

Site: DataLemur\
Difficulty per Site: Easy

## Problem

UnitedHealth Group (UHG) has a program called Advocate4Me, which allows policy holders (or, members) to call an advocate and receive support for their health care needs – whether that's claims and benefits support, drug coverage, pre- and post-authorisation, medical records, emergency assistance, or member portal services.

Write a query to find how many UHG policy holders made three, or more calls, assuming each call is identified by the case_id column. [[Full Description](https://datalemur.com/questions/frequent-callers)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT 
    policy_holder_id
  FROM callers
  GROUP BY policy_holder_id
  HAVING COUNT(policy_holder_id) >= 3
)
SELECT
  COUNT(policy_holder_id) AS policy_holder_count
FROM cte
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT 
  COUNT(policy_holder_id) AS policy_holder_count
FROM (
  SELECT
    policy_holder_id,
    COUNT(case_id) AS call_count
  FROM callers
  GROUP BY policy_holder_id
  HAVING COUNT(case_id) >= 3
) AS call_records;
```

## Notes

TODO

## NB

TBD

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
