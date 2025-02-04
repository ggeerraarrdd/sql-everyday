# SQL Everyday \#118

## User Activity for the Past 30 Days I

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to find the daily active user count for a period of `30` days ending `2019-07-27` inclusively. A user was active on someday if they made at least one activity on that day.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/user-activity-for-the-past-30-days-i/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    activity_date AS day
    ,COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date BETWEEN DATE('2019-07-28' - INTERVAL 30 DAY) AND '2019-07-28' 
GROUP BY activity_date
;
```

## Site Solution

```sql
-- LeetCode Solution 
SELECT 
    activity_date AS day, 
    COUNT(DISTINCT user_id) AS active_users
FROM 
    Activity
WHERE 
    DATEDIFF('2019-07-27', activity_date) < 30 AND DATEDIFF('2019-07-27', activity_date)>=0
GROUP BY 1
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
