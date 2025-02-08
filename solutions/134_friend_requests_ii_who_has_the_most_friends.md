# SQL Everyday \#134

## Friend Requests II: Who Has the Most Friends

Site: LeetCode\
Difficulty per Site: Medium

## Problem

Write a solution to find the people who have the most friends and the most friends number.

The test cases are generated so that only one person has the most friends. [[Full Description](https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
    SELECT
        accepter_id AS id
        ,COALESCE(COUNT(DISTINCT requester_id), 0) AS total
    FROM RequestAccepted
    GROUP BY accepter_id
),
cte2 AS (
    SELECT
    requester_id AS id
    ,COALESCE(COUNT(DISTINCT accepter_id), 0) AS total
FROM RequestAccepted
GROUP BY requester_id
),
cte3 AS (
    SELECT
        *
    FROM cte1 
    UNION ALL
    SELECT
        *
    FROM cte2
)
SELECT
    id
    ,SUM(total) AS num
FROM cte3
GROUP BY id
ORDER BY num DESC
LIMIT 1
;
```

## Site Solution

```sql
-- LeetCode Solution 
WITH all_ids AS (
   SELECT requester_id AS id 
   FROM RequestAccepted
   UNION ALL
   SELECT accepter_id AS id
   FROM RequestAccepted)
SELECT id, num
FROM 
   (
   SELECT id, 
      COUNT(id) AS num, 
      RANK () OVER(ORDER BY COUNT(id) DESC) AS rnk
   FROM all_ids
   GROUP BY id
   )t0
WHERE rnk=1
```

## Notes

TBD

## NB

`UNION ALL`

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)

