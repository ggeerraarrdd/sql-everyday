# SQL Everyday \#046

## 2nd Ride Delay

Site: DataLemur\
Difficulty per Site: Medium

## Problem

As a data analyst at Uber, it's your job to report the latest metrics for specific groups of Uber users. Some riders create their Uber account the same day they book their first ride; the rider engagement team calls them "in-the-moment" users.

Uber wants to know the average delay between the day of user sign-up and the day of their 2nd ride. Write a query to pull the average 2nd ride delay for "in-the-moment" Uber users. Round the answer to 2-decimal places. [[Full Description](https://datalemur.com/questions/2nd-ride-delay)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT
    r.user_id
    ,u.registration_date
    ,r.ride_date
    ,LEAD(r.ride_date, 1) OVER (PARTITION BY r.user_id ORDER BY r.ride_date ASC) AS lag_date
    ,ROW_NUMBER() OVER (PARTITION BY r.user_id ORDER BY r.ride_date ASC) AS rownum
  FROM rides AS r
  JOIN users AS u ON r.user_id = u.user_id
)
SELECT
  ROUND(SUM(lag_date - ride_date) / SUM(rownum), 2) AS average_delay
FROM cte
WHERE registration_date = ride_date
  AND lag_date IS NOT NULL 
  AND rownum = 1
;
```

## Site Solution

```sql
-- DataLemur Solution 
WITH moment_users AS (
  SELECT DISTINCT users.user_id
  FROM users 
  INNER JOIN rides
    ON users.user_id = rides.user_id
    AND users.registration_date = rides.ride_date
)
, rides_cte AS (
  SELECT 
    rides.user_id,
    rides.ride_date,
    ROW_NUMBER() OVER (
      PARTITION BY users.user_id 
      ORDER BY rides.ride_date) AS ride_nr,
    LAG(rides.ride_date) OVER (
      PARTITION BY users.user_id 
      ORDER BY rides.ride_date) AS lag_ride_date
  FROM moment_users AS users
  LEFT JOIN rides
    ON users.user_id = rides.user_id
)

SELECT ROUND(AVG(ride_date - lag_ride_date),2) AS average_delay
FROM rides_cte
WHERE ride_nr=2;
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
