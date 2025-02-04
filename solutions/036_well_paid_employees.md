# SQL Everyday \#036

## Well Paid Employees

Site: DataLemur\
Difficulty per Site: Easy

## Problem

Companies often perform salary analyses to ensure fair compensation practices. One useful analysis is to check if there are any employees earning more than their direct managers.

As a HR Analyst, you're asked to identify all employees who earn more than their direct managers. The result should include the employee's ID and name. [[Full Description](https://datalemur.com/questions/sql-well-paid-employees)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT 
  e1.employee_id
  ,e1.name AS employee_name
FROM employee AS e1
INNER JOIN employee AS e2 ON e1.manager_id = e2.employee_id
WHERE e1.salary > e2.salary
LIMIT 5;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT 
  emp.employee_id AS employee_id,
  emp.name AS employee_name
FROM employee AS mgr
INNER JOIN employee AS emp ON mgr.employee_id = emp.manager_id
WHERE emp.salary > mgr.salary;
```

## Notes

* This is a classic self-join problem involving hierarchical data (i.e., parent-child relationship). The foreign key is referring to the primary key in the same table.
* While `JOIN` can be used here, I like to use `INNER JOIN` when executing a self-join operation, and reserve `JOIN` for an inner join operation. Confusing, I know!
* In terms of readability, I probably would have used the same table aliases using in DataLemur's solution.

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
