# SQL Everyday \#112

## Percentage of Users Attended a Contest

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to find the percentage of the users registered in each contest rounded to *two decimals*.

Return the result table ordered by `percentage` in *descending order*. In case of a tie, order it by `contest_id` in *ascending order*. [[Full Description](https://leetcode.com/problems/percentage-of-users-attended-a-contest/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT 
    contest_id
    ,ROUND(COUNT(DISTINCT user_id) / (SELECT COUNT(user_id) FROM Users) * 100, 2) as percentage
FROM Register 
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC
;
```

## Site Solution

```sql
-- LeetCode Solution 
SELECT 
  contest_id, -- The ID of the contest
  ROUND(
    COUNT(DISTINCT user_id) * 100 / ( -- Calculate the percentage of users
      SELECT 
        COUNT(user_id) -- Total number of unique users
      FROM 
        Users
    ), 
    2
  ) AS percentage -- The percentage of users registered for each contest, rounded to 2 decimal places
FROM 
  Register -- The table containing registration information
GROUP BY 
  contest_id -- Group the data by contest ID
ORDER BY 
  percentage DESC, -- Order the results by percentage in descending order
  contest_id; -- Then order by contest ID for ties
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
