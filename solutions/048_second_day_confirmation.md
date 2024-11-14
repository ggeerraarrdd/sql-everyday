# SQL Everyday \#048

## Second Day Confirmation

Site: DataLemur\
Difficulty per Site: Easy

## Problem

Assume you're given tables with information about TikTok user sign-ups and confirmations through email and text. New users on TikTok sign up using their email addresses, and upon sign-up, each user receives a text message confirmation to activate their account.

Write a query to display the user IDs of those who did not confirm their sign-up on the first day, but confirmed on the second day. [[Full Description](https://datalemur.com/questions/second-day-confirmation)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT 
  DISTINCT user_id 
FROM emails AS e
JOIN texts AS t ON e.email_id = t.email_id
WHERE t.signup_action = 'Confirmed'
  AND t.action_date = e.signup_date + INTERVAL '1 day'
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT DISTINCT user_id
FROM emails 
INNER JOIN texts
  ON emails.email_id = texts.email_id
WHERE texts.action_date = emails.signup_date + INTERVAL '1 day'
  AND texts.signup_action = 'Confirmed';
```

## Notes

* SQL Server: `WHERE call_date = DATEADD(day, 1, e.signup_date)`
* MySQL: `WHERE call_date = DATE_ADD(e.signup_date), INTERVAL 1 DAY)`

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
