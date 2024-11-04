# SQL Everyday \#038

## Department vs. Company Salary

Site: DataLemur\
Difficulty per Site: Hard

## Problem

You work as a data analyst for a FAANG company that tracks employee salaries over time. The company wants to understand how the average salary in each department compares to the company's overall average salary each month.

Write a query to compare the average salary of employees in each department to the company's average salary for March 2024. Return the comparison result as 'higher', 'lower', or 'same' for each department. Display the department ID, payment month (in MM-YYYY format), and the comparison result. [[Full Description](https://datalemur.com/questions/sql-department-company-salary-comparison)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT 
    employee.department_id
    ,salary.employee_id
    ,salary.amount
    ,salary.payment_date
    ,AVG(amount) OVER (PARTITION BY department_id) AS salary_employees
    ,AVG(amount) OVER () AS salary_company
    ,ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary.employee_id ASC) AS rownum
  FROM salary
  JOIN employee ON salary.employee_id = employee.employee_id
  WHERE payment_date BETWEEN '03/01/2024' AND '04/01/2024'
)
SELECT
  department_id
  ,TO_CHAR(payment_date, 'MM-YYYY') AS payment_date
  ,CASE 
    WHEN salary_employees < salary_company THEN 'lower'
    WHEN salary_employees > salary_company THEN 'higher'
    ELSE 'same'
    END AS comparison
FROM cte
WHERE rownum = 1
;
```

## Site Solution

```sql
-- DataLemur Solution 
WITH company_avg AS ( -- CTE from Step 1
  SELECT 
    payment_date,
    AVG(amount) AS co_avg_salary
  FROM salary
  WHERE payment_date = '03/31/2024 00:00:00'
  GROUP BY payment_date
)
, dept_avg AS ( -- CTE from Step 2
  SELECT
    e.department_id,
    s.payment_date,
    AVG(s.amount) AS dept_avg_salary
  FROM salary AS s
  INNER JOIN employee AS e
    ON s.employee_id = e.employee_id
  WHERE s.payment_date = '03/31/2024 00:00:00'
  GROUP BY e.department_id, s.payment_date
)

SELECT
  d.department_id,
  TO_CHAR(d.payment_date, 'MM-YYYY') AS payment_date,
  CASE  
    WHEN d.dept_avg_salary > c.co_avg_salary THEN 'higher'
    WHEN d.dept_avg_salary < c.co_avg_salary THEN 'lower'
    ELSE 'same'
  END AS comparison
FROM dept_avg AS d
INNER JOIN company_avg AS c
  ON d.payment_date = c.payment_date;
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
