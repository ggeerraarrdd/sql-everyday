# SQL Everyday \#008

## Signup Activation Rate

Site: DataLemur\
Difficulty per Site: Medium

## Problem

New TikTok users sign up with their emails. They confirmed their signup by replying to the text confirmation to activate their accounts. Users may receive multiple text messages for account confirmation until they have confirmed their new account. A senior analyst is interested to know the activation rate of specified users in the emails table. Write a query to find the activation rate. Round the percentage to 2 decimal places. [[Full Description](https://datalemur.com/questions/signup-confirmation-rate)]

## Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT 
    COUNT(signup_action) FILTER (WHERE signup_action = 'Confirmed')::decimal AS confirmed
    ,COUNT(signup_action) FILTER (WHERE signup_action = 'Not Confirmed')::decimal AS not_confirmed
  FROM emails AS e
  JOIN texts AS t ON e.email_id = t.email_id
)
SELECT
  ROUND(confirmed / (confirmed + not_confirmed), 2) AS confirm_rate
FROM cte
;

-- DataLemur Solution
SELECT 
  ROUND(COUNT(texts.email_id)::DECIMAL / COUNT(DISTINCT emails.email_id), 2) AS activation_rate
FROM emails
LEFT JOIN texts ON emails.email_id = texts.email_id AND texts.signup_action = 'Confirmed'
;  
```

## Notes

* The key to getting the right result is casting the values as decimal, otherwise you'll get `0`.

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
