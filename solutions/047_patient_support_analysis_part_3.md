# SQL Everyday \#047

## Patient Support Analysis (Part 3)

Site: DataLemur\
Difficulty per Site: Hard

## Problem

UnitedHealth Group (UHG) has a program called Advocate4Me, which allows policy holders (or, members) to call an advocate and receive support for their health care needs – whether that's claims and benefits support, drug coverage, pre- and post-authorisation, medical records, emergency assistance, or member portal services.

Write a query to obtain the number of unique callers who made calls within a 7-day interval of their previous calls. If a caller made more than two calls within the 7-day period, count them only once. [[Full Description](https://datalemur.com/questions/patient-call-history)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
SELECT
  policy_holder_id
  ,EXTRACT(DAY FROM LAG(call_date, 1) OVER (PARTITION BY policy_holder_id ORDER BY call_date ASC) - call_date) AS days
FROM callers
)
SELECT
  COUNT(DISTINCT policy_holder_id) AS policy_holder_count
FROM cte
WHERE days IS NOT NULL 
  AND days > -7
;
```

## Site Solution

```sql
-- DataLemur Solution 
-- Solution #1
WITH call_history AS (
  SELECT
    policy_holder_id,
    call_date AS current_call, -- Remove this column
    LAG(call_date) OVER (
  	  PARTITION BY policy_holder_id ORDER BY call_date) AS previous_call, -- Remove this column
    ROUND(EXTRACT(EPOCH FROM call_date 
      - LAG(call_date) OVER (
  	    PARTITION BY policy_holder_id ORDER BY call_date)
    )/(24*60*60),2) AS time_diff_days
  FROM callers
)

SELECT COUNT(DISTINCT policy_holder_id) AS policy_holder_count
FROM call_history
WHERE time_diff_days <= 7;

-- Solution #2: Using INTERVAL
WITH call_history AS (
  SELECT 
    policy_holder_id,
    call_date AS current_call,
    LEAD(call_date) OVER (
      PARTITION BY policy_holder_id ORDER BY call_date) AS next_call
  FROM callers
)

SELECT COUNT(DISTINCT policy_holder_id) AS policy_holder_count
FROM call_history
WHERE current_call + INTERVAL '168 hours' >= next_call;
```

## Notes

TODO

## NB

TBD

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
