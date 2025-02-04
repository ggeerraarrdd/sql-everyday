# SQL Everyday \#014

## International Call Percentage

Site: DataLemur\
Difficulty per Site: Medium

## Problem

A phone call is considered an international call when the person calling is in a different country than the person receiving the call. What percentage of phone calls are international? Round the result to 1 decimal. [[Full Description](https://datalemur.com/questions/international-call-percentage)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT 
    caller.country_id AS caller_country
    ,receiver.country_id AS receiver_country
  FROM phone_calls AS calls 
  JOIN phone_info AS caller ON calls.caller_id = caller.caller_id
  JOIN phone_info AS receiver ON calls.receiver_id = receiver.caller_id
)
SELECT
  ROUND(100 * COUNT(caller_country) FILTER (WHERE caller_country <> receiver_country)::decimal / COUNT(caller_country)::decimal, 1) AS international_calls_pct
FROM cte
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT 
  ROUND(
    100.0 * SUM(CASE
      WHEN caller.country_id <> receiver.country_id THEN 1 ELSE NULL END)
    /COUNT(*) ,1) AS international_call_pct
FROM phone_calls AS calls
LEFT JOIN phone_info AS caller
  ON calls.caller_id = caller.caller_id
LEFT JOIN phone_info AS receiver
  ON calls.receiver_id = receiver.caller_id;
```

## Notes

* Differences between solutions:
  * CTE vs no CTE
  * `FILTER()` vs `CASE`
  * Casting to decimal with `::` vs multiplying with a decimal (100 vs 100.0)
* Using a CTE here is a personal style preference.

## NB

TBD

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
