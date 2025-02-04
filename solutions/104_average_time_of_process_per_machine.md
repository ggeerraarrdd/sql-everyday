# SQL Everyday \#104

## Average Time of Process per Machine

Site: LeetCode\
Difficulty per Site: Easy

## Problem

There is a factory website that has several machines each running the *same number of processes*. Write a solution to find the *average time* each machine takes to complete a process.

The time to complete a process is the `'end' timestamp` minus the `'start' timestamp`. The average time is calculated by the total time to complete every process on the machine divided by the number of processes that were run.

The resulting table should have the `machine_id` along with the average time as `processing_time`, which should be rounded to 3 decimal places.

Return the resulting table in *any order*. [[Full Description](https://leetcode.com/problems/average-time-of-process-per-machine/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
    SELECT * 
    FROM Activity
    WHERE activity_type = 'start'
),
cte2 AS (
    SELECT * 
    FROM Activity
    WHERE activity_type = 'end'
)
SELECT 
    c1.machine_id,
    ROUND(AVG(c2.timestamp - c1.timestamp), 3) AS processing_time
FROM cte1 as c1
JOIN cte2 as c2 ON c1.machine_id = c2.machine_id
    AND c1.process_id = c2.process_id
GROUP BY c1.machine_id
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- Approach 1: Transform Values with `CASE WHEN` and then Calculate
SELECT 
    machine_id,
    ROUND(SUM(CASE WHEN activity_type='start' THEN timestamp*-1 ELSE timestamp END)*1.0
    / (SELECT COUNT(DISTINCT process_id)),3) AS processing_time
FROM 
    Activity
GROUP BY machine_id

-- Approach 2: Calling the original Table twice and Calculate as two columns
SELECT a.machine_id, 
       ROUND(AVG(b.timestamp - a.timestamp), 3) AS processing_time
FROM Activity a, 
     Activity b
WHERE 
    a.machine_id = b.machine_id
AND 
    a.process_id = b.process_id
AND 
    a.activity_type = 'start'
AND 
    b.activity_type = 'end'
GROUP BY machine_id
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
