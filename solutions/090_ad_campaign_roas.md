# SQL Everyday \#090

## Ad Campaign ROAS

Site: DataLemur\
Difficulty per Site: Easy

## Problem

Google marketing managers are analyzing the performance of various advertising accounts over the last month. They need your help to gather the relevant data.

Write a query to calculate the return on ad spend (ROAS) for each advertiser across all ad campaigns. Round your answer to 2 decimal places, and order your output by the `advertiser_id`.

Hint: ROAS = Ad Revenue / Ad Spend [[Full Description](https://datalemur.com/questions/ad-campaign-roas)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT
    advertiser_id
    ,SUM(spend) AS spend
    ,SUM(revenue) AS revenue
  FROM ad_campaigns
  GROUP BY advertiser_id
)
SELECT
  advertiser_id
  ,ROUND((revenue / spend)::DECIMAL, 2) AS ROAS
FROM cte
ORDER BY advertiser_id ASC
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT
  advertiser_id,
  ROUND(((SUM(revenue) / SUM(spend))::DECIMAL), 2) AS ROAS
FROM ad_campaigns
GROUP BY advertiser_id
ORDER BY advertiser_id;
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
