# SQL Everyday \#006

## Top Three Salaries

Site: DataLemur\
Difficulty per Site: Medium

## Problem

As part of an ongoing analysis of salary distribution within the company, your manager has requested a report identifying high earners in each department. A 'high earner' within a department is defined as an employee with a salary ranking among the top three salaries within that department.

You're tasked with identifying these high earners across all departments. Write a query to display the employee's name along with their department name and salary. In case of duplicates, sort the results of department name in ascending order, then by salary in descending order. If multiple employees have the same salary, then order them alphabetically. [[Full Description](https://datalemur.com/questions/sql-top-three-salaries)]

## Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT 
    d.department_name
    ,e.name
    ,e.salary
    ,DENSE_RANK() OVER (PARTITION BY d.department_name ORDER BY e.salary DESC) AS salary_rank
  FROM employee AS e 
  JOIN department AS d ON e.department_id = d.department_id
)
SELECT
  department_name
  ,name
  ,salary
FROM cte 
WHERE salary_rank <= 3
ORDER BY department_name ASC, salary DESC, name ASC  
;
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
