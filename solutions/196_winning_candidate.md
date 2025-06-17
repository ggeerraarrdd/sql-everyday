# SQL Everyday \#196

## Winning Candidate

Site: LeetCode\
Difficulty per Site: Medium

## Problem

Write a solution to report the name of the winning candidate (i.e., the candidate who got the largest number of votes).

The test cases are generated so that **exactly one candidate wins** the elections. [[Full Description](https://leetcode.com/problems/winning-candidate/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
    SELECT
        c.name
        ,COUNT(v.id) AS votes
    FROM Vote AS v
    JOIN Candidate AS c ON v.candidateId = c.id
    GROUP BY c.name
    ORDER BY votes DESC
    LIMIT 1
)
SELECT
    name
FROM cte
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- Site solution essentially the same
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
