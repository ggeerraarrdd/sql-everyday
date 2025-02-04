# SQL Everyday \#093

## Webinar Popularity

Site: DataLemur\
Difficulty per Site: Easy

## Problem

As a Data Analyst on Snowflake's Marketing Analytics team, you're analyzing the CRM to determine what percent of marketing touches were of type "webinar" in April 2022. Round your percentage to the nearest integer.

Did you know? Marketing touches, also known as touch points are the brand's (Snowflake's) point of contact with the customers, from start to finish. [[Full Description](https://datalemur.com/questions/snowflake-webinar-popularity)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
  100 * COUNT(*) FILTER (WHERE event_type = 'webinar') / COUNT(*) AS webinar_pct
FROM marketing_touches
WHERE event_date BETWEEN '04/01/2022' AND '05/01/2022'
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT 
  ROUND(100 *
    SUM(CASE WHEN event_type='webinar' THEN 1 ELSE 0 END)/
    COUNT(*)) as webinar_pct
FROM marketing_touches
WHERE DATE_TRUNC('month', event_date) = '04/01/2022';
```

## Notes

TODO

## NB

`DATE_TRUNC()` vs `BETWEEN`

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
