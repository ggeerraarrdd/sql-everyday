# SQL Everyday \#003

## Second Highest Salary

Site: DataLemur\
Difficulty per Site: Medium

## Problem

Your manager is keen on understanding the pay distribution and asks you to determine the second highest salary among all employees. It's possible that multiple employees may share the same second highest salary. In case of duplicate, display the salary only once. [[Full Description](https://datalemur.com/questions/sql-second-highest-salary)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT
    employee_id
    ,salary
    ,DENSE_RANK() OVER (ORDER BY salary DESC) AS rank
  FROM employee
)
SELECT
  salary AS second_highest_salary
FROM cte 
WHERE rank = 2
LIMIT 1
;
```

## Site Solution

```sql
-- DataLemur Solution
SELECT MAX(salary) AS second_highest_salary
FROM employee
WHERE salary < (
    SELECT MAX(salary)
    FROM employee
);
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
