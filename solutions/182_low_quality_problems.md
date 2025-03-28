# SQL Everyday \#182

## Low-Quality Problems

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Find the IDs of the **low-quality problems**. A LeetCode problem is **low-quality** if the like percentage of the problem (number of likes divided by the total number of votes) is **strictly less than** `60%`.

Return the result table ordered by `problem_id` in ascending order. [[Full Description](https://leetcode.com/problems/low-quality-problems/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    problem_id
FROM (
    SELECT
        problem_id
        ,1.00 * likes / (likes + dislikes) AS quality
    FROM Problems
) AS p
WHERE quality < .6
ORDER BY problem_id ASC
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- None

-- Code Author: byuns9334
-- https://leetcode.com/problems/low-quality-problems/solutions/1562160/simple-mssql
SELECT
    a.problem_id
FROM Problems AS a 
WHERE a.likes * 2 < a.dislikes * 3
ORDER BY a.problem_id ASC
;

-- Code Author: Parantika
-- https://leetcode.com/problems/low-quality-problems/solutions/1499691/ms-sql
SELECT
    problem_id
FROM problems
WHERE likes / cast((likes + dislikes) AS float) < 0.6
ORDER BY problem_id
;
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
