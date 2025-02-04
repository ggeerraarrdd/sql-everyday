# SQL Everyday \#027

## Laptop vs. Mobile Viewership

Site: DataLemur\
Difficulty per Site: Easy

## Problem

Assume you're given the table on user viewership categorised by device type where the three types are laptop, tablet, and phone.

Write a query that calculates the total viewership for laptops and mobile devices where mobile is defined as the sum of tablet and phone viewership. Output the total viewership for laptops as `laptop_reviews` and the total viewership for mobile devices as `mobile_views`. [[Full Description](https://datalemur.com/questions/laptop-mobile-viewership)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT 
  sender_id
  ,COUNT(sender_id) AS message_count
FROM messages
WHERE sent_date BETWEEN '08/01/2022' AND '09/01/2022'
GROUP BY sender_id
ORDER BY message_count DESC
LIMIT 2
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT 
  SUM(CASE WHEN device_type = 'laptop' THEN 1 ELSE 0 END) AS laptop_views, 
  SUM(CASE WHEN device_type IN ('tablet', 'phone') THEN 1 ELSE 0 END) AS mobile_views 
FROM viewership;
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
