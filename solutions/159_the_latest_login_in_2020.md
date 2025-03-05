# SQL Everyday \#159

## The Latest Login in 2020

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to report the *latest* login for all users in the year `2020`. Do *not* include the users who did not login in `2020`.

Return the result table *in any order*. [[Full Description](https://leetcode.com/problems/the-latest-login-in-2020/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    user_id
    ,MAX(time_stamp) AS last_stamp
FROM Logins
WHERE time_stamp BETWEEN '2020-01-01 00:00:00' AND '2020-12-31 23:59:59'
GROUP BY user_id
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- Solution 1: Using YEAR() to extract year from the date column and MAX() to find the latest record
SELECT 
    user_id, 
    MAX(time_stamp) AS last_stamp
FROM 
    Logins
WHERE 
    YEAR(time_stamp) = 2020
GROUP BY 1;

-- Solution 2: Using EXTRACT() to get year from the date column and FIRST_VALUE() to find the latest record
SELECT
    DISTINCT user_id,
    FIRST_VALUE(time_stamp)OVER(PARTITION BY user_id ORDER BY time_stamp DESC) AS last_stamp
FROM
    Logins
WHERE EXTRACT(Year FROM time_stamp) = 2020;
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
