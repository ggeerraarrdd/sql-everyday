# SQL Everyday \#143

## Rank Scores

Site: LeetCode\
Difficulty per Site: Medium

## Problem

Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules:

* The scores should be ranked from the highest to the lowest.
* If there is a tie between two scores, both should have the same ranking.
* After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.

Return the result table ordered by `score` in descending order. [[Full Description](https://leetcode.com/problems/rank-scores/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    score
    ,DENSE_RANK() OVER (ORDER BY score DESC) AS rank
FROM Scores
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- TBD
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
