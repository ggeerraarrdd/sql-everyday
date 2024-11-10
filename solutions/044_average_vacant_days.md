# SQL Everyday \#044

## Average Vacant Days

Site: DataLemur\
Difficulty per Site: Hard

## Problem

The strategy team in Airbnb is trying to analyze the impact of Covid-19 during 2021. To do so, they need you to write a query that outputs the average vacant days across the AirBnbs in 2021. Some properties have gone out of business, so you should only analyze rentals that are currently active. Round the results to a whole number. [[Full Description](https://datalemur.com/questions/average-vacant-days)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
  SELECT
    l.listing_id
    ,CASE 
      WHEN b.checkin_date IS NULL THEN null 
      WHEN EXTRACT(YEAR FROM b.checkin_date) = 2021 THEN b.checkin_date 
      ELSE '01/01/2021' 
      END AS checkin_date_mod
    ,CASE 
      WHEN b.checkout_date IS NULL THEN null 
      WHEN EXTRACT(YEAR FROM b.checkout_date) = 2021 THEN b.checkout_date 
      ELSE '12/31/2021' 
      END AS checkout_date_mod
  FROM listings AS l
  LEFT JOIN bookings AS b ON l.listing_id = b.listing_id
  WHERE l.is_active = 1
    AND (EXTRACT(YEAR FROM b.checkin_date) = 2021 OR EXTRACT(YEAR FROM b.checkout_date) = 2021)
    OR (b.checkin_date IS NULL OR b.checkout_date IS NULL)
),
cte2 AS (
  SELECT
    listing_id
    ,COALESCE(365 - SUM(checkout_date_mod - checkin_date_mod), 365) AS days
  FROM cte1
  GROUP BY listing_id
)
SELECT
  ROUND(AVG(days), 0) AS avg_vacant_days
FROM cte2
;
```

## Site Solution

```sql
-- DataLemur Solution 
WITH listing_vacancies AS (
SELECT 
  listings.listing_id,
  365 - COALESCE(
    SUM(
      CASE WHEN checkout_date>'12/31/2021' THEN '12/31/2021' ELSE checkout_date END -
      CASE WHEN checkin_date<'01/01/2021' THEN '01/01/2021' ELSE checkin_date END 
  ),0) AS vacant_days
FROM listings 
LEFT JOIN bookings
  ON listings.listing_id = bookings.listing_id 
WHERE listings.is_active = 1
GROUP BY listings.listing_id)

SELECT ROUND(AVG(vacant_days)) 
FROM listing_vacancies;
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
