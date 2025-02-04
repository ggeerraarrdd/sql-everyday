# SQL Everyday \#050

## Patient Support Analysis (Part 4)

Site: DataLemur\
Difficulty per Site: Hard

## Problem

UnitedHealth Group (UHG) has a program called Advocate4Me, which allows policy holders (or, members) to call an advocate and receive support for their health care needs – whether that's claims and benefits support, drug coverage, pre- and post-authorisation, medical records, emergency assistance, or member portal services.

To analyze the performance of the program, write a query to determine the month-over-month growth rate specifically for long-calls. A long-call is defined as any call lasting more than 5 minutes (300 seconds).

Output the year and month in numerical format and chronological order, along with the growth percentage rounded to 1 decimal place. [[Full Description](https://datalemur.com/questions/long-calls-growth)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
  SELECT
    DATE_TRUNC('month', call_date) AS yr_mth
    ,COUNT(case_id) AS long_calls_count
  FROM callers
  WHERE call_duration_secs > 300
  GROUP BY yr_mth
)
SELECT
  EXTRACT(YEAR FROM yr_mth) AS yr
  ,EXTRACT(MONTH FROM yr_mth) AS mth
  ,ROUND(100.0 * (long_calls_count - LAG(long_calls_count, 1) OVER (ORDER BY yr_mth)) / LAG(long_calls_count, 1) OVER (ORDER BY yr_mth), 1) AS diff_per
FROM cte1
;
```

## Site Solution

```sql
-- DataLemur Solution 
WITH long_calls AS (
  SELECT 
    EXTRACT(YEAR FROM call_date) AS yr,
    EXTRACT(MONTH FROM call_date) AS mth,
    COUNT(case_id) AS curr_mth_calls,
    LAG(COUNT(case_id)) OVER (
      ORDER BY EXTRACT(MONTH FROM call_date)) AS prev_mth_calls
FROM callers
WHERE call_duration_secs > 300
GROUP BY 
  EXTRACT(YEAR FROM call_date),
  EXTRACT(MONTH FROM call_date)
)

SELECT
  yr,
  mth,
  ROUND(100.0 * 
    (curr_mth_calls - prev_mth_calls)/prev_mth_calls,1) AS long_calls_growth_pct
FROM long_calls
ORDER BY yr, mth;
```

## Notes

TODO

## NB

TBD

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
