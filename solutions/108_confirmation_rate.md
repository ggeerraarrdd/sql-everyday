# SQL Everyday \#108

## Confirmation Rate

Site: LeetCode\
Difficulty per Site: Medium

## Problem

The *confirmation rate* of a user is the number of `'confirmed'` messages divided by the total number of requested confirmation messages. The confirmation rate of a user that did not request any confirmation messages is 0. Round the confirmation rate to *two decimal* places.

Write a solution to find the *confirmation rate* of each user.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/confirmation-rate/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT 
    s.user_id
    ,ROUND(SUM(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END) / COUNT(s.user_id), 2) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c ON s.user_id = c.user_id
GROUP BY s.user_id
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- None provided
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
