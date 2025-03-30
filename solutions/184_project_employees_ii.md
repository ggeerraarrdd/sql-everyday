# SQL Everyday \#184

## Project Employees II

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to report all the projects that have the most employees.

Return the resulting table in **any order**. [[Full Description](https://leetcode.com/problems/project-employees-ii/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
    SELECT
        p.project_id
        ,COUNT(DISTINCT p.employee_id) AS emp_count
    FROM Project AS p
    JOIN Employee AS e ON p.employee_id = e.employee_id
    GROUP BY p.project_id
),
cte2 AS (
    SELECT
        project_id
        ,RANK() OVER (ORDER BY emp_count DESC) AS ranked
    FROM cte1
)
SELECT
    project_id
FROM cte2
WHERE ranked = 1
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- None

-- Code Author: Jingjing Chen
-- https://leetcode.com/problems/project-employees-ii/solutions/1096599/smart-window-function-solution-please-take-a-look
WITH CTE AS (
SELECT project_id, RANK() OVER(ORDER BY COUNT(employee_id) DESC) as ranking
FROM Project
GROUP BY project_id
    )
    
SELECT project_id
FROM CTE
WHERE ranking = 1
ORDER BY project_id;

-- Code Author: Merciless
-- https://leetcode.com/problems/project-employees-ii/solutions/307641/simple-sql-solution
SELECT project_id
FROM project
GROUP BY project_id
HAVING COUNT(employee_id) =
(
    SELECT count(employee_id)
    FROM project
    GROUP BY project_id
    ORDER BY count(employee_id) desc
    LIMIT 1
)

-- Code Author: Yaroslav Trofimov
-- https://leetcode.com/problems/project-employees-ii/solutions/1476031/MAX
SELECT project_id
FROM Project
GROUP BY project_id
HAVING COUNT(employee_id) = (
    SELECT MAX(employees_count.employees_per_project)
    FROM (
        SELECT COUNT(employee_id) as employees_per_project
        FROM Project
        GROUP BY project_id
    ) employees_count
)
```

## Notes

TBD

## NB

Window function w/ `GROUP BY`

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
