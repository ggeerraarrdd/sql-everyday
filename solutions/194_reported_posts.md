# SQL Everyday \#194

## Reported Posts

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to report the number of posts reported yesterday for each report reason. Assume today is `2019-07-05`.

Return the result table in **any order**. [[Full Description](https://leetcode.com/problems/reported-posts/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
    SELECT 
        DISTINCT post_id
        ,action_date
        ,action
        ,extra 
    FROM Actions
    WHERE action_date =  DATE '2019-07-05' - INTERVAL '1 day'
        AND action = 'report'
)
SELECT 
	extra AS report_reason
    ,COUNT(extra) AS report_count 
FROM CTE
GROUP BY extra
;
```

## Site Solution

```sql
-- LeetCode Solution 
SELECT
    extra AS report_reason,
    COUNT(DISTINCT post_id) AS report_count
FROM Actions
WHERE action_date = '2019-07-04' AND 
      action = 'report'
GROUP BY report_reason;
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
