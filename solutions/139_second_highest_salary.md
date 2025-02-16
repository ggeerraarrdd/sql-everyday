# SQL Everyday \#139

## Second Highest Salary

Site: LeetCode\
Difficulty per Site: Medium

## Problem

Write a solution to find the second highest *distinct* salary from the `Employee` table. If there is no second highest salary, return `null (return None in Pandas)`. [[Full Description](https://leetcode.com/problems/second-highest-salary/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
    SELECT
        DISTINCT salary
    FROM Employee
),
cte2 AS (
    SELECT
        salary
        ,ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num
        ,COUNT(*) OVER () AS row_count
    FROM cte1
)
SELECT
    CASE WHEN row_count >= 2 THEN (SELECT salary FROM cte2 WHERE row_num = 2) ELSE null END AS SecondHighestSalary
FROM cte2
LIMIT 1
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
