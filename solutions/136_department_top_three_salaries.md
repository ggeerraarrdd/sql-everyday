# SQL Everyday \#136

## Department Top Three Salaries

Site: LeetCode\
Difficulty per Site: Hard

## Problem

A company's executives are interested in seeing who earns the most money in each of the company's departments. A *high earner* in a department is an employee who has a salary in the *top three unique* salaries for that department.

Write a solution to find the employees who are *high earners* in each of the departments.

Return the result table *in any order*. [[Full Description](https://leetcode.com/problems/department-top-three-salaries/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
    SELECT
        d.name AS Department
        ,e.name AS Employee
        ,e.salary AS Salary
        ,DENSE_RANK() OVER (PARTITION BY d.name ORDER BY e.salary DESC) AS rank
    FROM Employee AS e
    JOIN Department AS d ON e.departmentId = d.id
)
SELECT
    Department
    ,Employee
    ,Salary
FROM cte
WHERE rank <= 3
ORDER BY Department ASC, Employee ASC, Salary DESC
;
```

## Site Solution

```sql
-- LeetCode Solution 
SELECT d.name AS 'Department', 
       e1.name AS 'Employee', 
       e1.salary AS 'Salary' 
FROM Employee e1
JOIN Department d
ON e1.departmentId = d.id 
WHERE
    3 > (SELECT COUNT(DISTINCT e2.salary)
        FROM Employee e2
        WHERE e2.salary > e1.salary AND e1.departmentId = e2.departmentId);
```

## Notes

TBD

## NB



Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)

