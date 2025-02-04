# SQL Everyday \#045

## App Click-through Rate (CTR)

Site: DataLemur\
Difficulty per Site: Easy

## Problem

Assume you have an events table on Facebook app analytics. Write a query to calculate the click-through rate (CTR) for the app in 2022 and round the results to 2 decimal places. [[Full Description](https://datalemur.com/questions/click-through-rate)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT 
    app_id
    ,COUNT(event_type) FILTER (WHERE event_type = 'click') AS clicks
    ,COUNT(event_type) FILTER (WHERE event_type = 'impression') AS impressions
  FROM events
  WHERE EXTRACT(YEAR FROM timestamp) = 2022
  GROUP BY app_id
)
SELECT 
  app_id
  ,ROUND(100.0 * clicks / impressions, 2) AS ctr
FROM cte
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT
  app_id,
  ROUND(100.0 *
    SUM(CASE WHEN event_type = 'click' THEN 1 ELSE 0 END) /
    SUM(CASE WHEN event_type = 'impression' THEN 1 ELSE 0 END), 2)  AS ctr_rate
FROM events
WHERE timestamp >= '2022-01-01' 
  AND timestamp < '2023-01-01'
GROUP BY app_id;
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
