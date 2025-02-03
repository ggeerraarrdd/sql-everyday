# SQL Everyday \#128

## Last Person to Fit in the Bus

Site: LeetCode\
Difficulty per Site: Medium

## Problem

There is a queue of people waiting to board a bus. However, the bus has a weight limit of `1000` *kilograms*, so there may be some people who cannot board.

Write a solution to find the `person_name` of the *last person* that can fit on the bus without exceeding the weight limit. The test cases are generated such that the first person does not exceed the weight limit.

*Note* that *only one* person can board the bus at any given turn. [[Full Description](https://leetcode.com/problems/last-person-to-fit-in-the-bus/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
    SELECT
    *
    ,SUM(weight) OVER (ORDER BY turn RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS total
    FROM Queue
)
SELECT
    person_name
FROM cte
WHERE total <= 1000
ORDER BY total DESC
LIMIT 1
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- None
```

## Notes

TBD

## NB

`ORDER BY turn RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`

Go to [Table of Contents](/README.md#contents)
Go to [Overview](/README.md)
