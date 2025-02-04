# SQL Everyday \#040

## Booking Referral Source

Site: DataLemur\
Difficulty per Site: Medium

## Problem

The Airbnb marketing analytics team is trying to understand what are the most common marketing channels that lead users to book their first rental on Airbnb.

Write a query to find the top marketing channel and percentage of first rental bookings from the aforementioned marketing channel. Round the percentage to the closest integer. Assume there are no ties. [[Full Description](https://datalemur.com/questions/booking-referral-source)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
  SELECT
    b.user_id
    ,b.booking_date
    ,a.channel
    ,ROW_NUMBER() OVER (PARTITION BY b.user_id ORDER BY booking_date ASC) AS booking_first
  FROM bookings AS b
  JOIN booking_attribution AS a ON b.booking_id = a.booking_id
),
cte2 AS (
  SELECT
    *
    ,COUNT(booking_first) OVER (PARTITION BY channel) AS channel_count
    ,COUNT(booking_first) OVER () AS total_count
  FROM cte1
  WHERE booking_first = 1
  ORDER BY channel
)
SELECT
  DISTINCT channel
  ,ROUND(100.0 * channel_count / total_count, 0) AS first_booking_pct
FROM cte2
ORDER BY first_booking_pct DESC
LIMIT 1
; 
```

## Site Solution

```sql
-- DataLemur Solution 
WITH user_bookings AS (
    SELECT 
        bookings.booking_id,
        ROW_NUMBER() OVER (PARTITION BY bookings.user_id ORDER BY bookings.booking_date) AS booking_no,
        channels.channel
    FROM bookings
    INNER JOIN booking_attribution AS channels
    ON bookings.booking_id = channels.booking_id
), 
first_bookings AS (
    SELECT 
        channel, 
        COUNT(*) AS channel_booking
    FROM user_bookings
    WHERE booking_no = 1
    GROUP BY channel
)

SELECT 
  channel, 
  ROUND(100.0 * (channel_booking / (SELECT SUM(channel_booking) FROM first_bookings)), 0) AS first_booking_pct
FROM first_bookings
WHERE channel IS NOT NULL
ORDER BY first_booking_pct DESC
LIMIT 1;
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
