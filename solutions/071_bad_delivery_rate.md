# SQL Everyday \#071

## Bad Delivery Rate

Site: DataLemur\
Difficulty per Site: Hard

## Problem

The Growth Team at DoorDash wants to ensure that new users, who make orders within their first 14 days on the platform, have a positive experience. However, they have noticed several issues with deliveries that result in a bad experience.

These issues include:
* Orders being completed incorrectly, with missing items or wrong orders.
* Orders not being received due to incorrect addresses or drop-off spots.
* Orders being delivered late, with the actual delivery time being 30 minutes later than the order placement time. Note that the `estimated_delivery_timestamp` is automatically set to 30 minutes after the `order_timestamp`.

Write a query that calculates the bad experience rate for new users who signed up in June 2022 during their first 14 days on the platform. The output should include the percentage of bad experiences, rounded to 2 decimal places. [[Full Description](https://datalemur.com/questions/sql-bad-experience)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT
    o.order_id
    ,CASE WHEN status = 'completed successfully' THEN 0 ELSE 1 END AS status_num
  FROM orders AS o 
  JOIN trips AS t ON o.trip_id = t.trip_id
  JOIN customers AS c ON o.customer_id = c.customer_id
  WHERE c.signup_timestamp BETWEEN '06/01/2022' AND '07/01/2022'
    AND EXTRACT(DAY FROM o.order_timestamp - c.signup_timestamp) <= 14
  ORDER BY o.customer_id ASC
)
SELECT
  ROUND(100.0 * SUM(status_num) / COUNT(order_id), 2) AS bad_experience_pct
FROM cte
; 
```

## Site Solution

```sql
-- DataLemur Solution 
WITH june22_cte AS (
SELECT 
  orders.order_id,
  orders.trip_id,
  orders.status
FROM customers
INNER JOIN orders
  ON customers.customer_id = orders.customer_id
WHERE EXTRACT(MONTH FROM customers.signup_timestamp) = 6
  AND EXTRACT(YEAR FROM customers.signup_timestamp) = 2022
  AND orders.order_timestamp BETWEEN customers.signup_timestamp 
    AND customers.signup_timestamp + INTERVAL '14 DAYS'
)

SELECT 
  ROUND(
    100.0 *
      COUNT(june22.order_id)
      / (SELECT COUNT(order_id) FROM june22_cte)
  ,2) AS bad_experience_pct
FROM june22_cte AS june22
INNER JOIN trips
  ON june22.trip_id = trips.trip_id
WHERE june22.status IN ('completed incorrectly', 'never received');
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
