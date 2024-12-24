# SQL Everyday \#088

## Compensation Outliers

Site: DataLemur\
Difficulty per Site: Medium

## Problem

Your team at Accenture is helping a Fortune 500 client revamp their compensation and benefits program. The first step in this analysis is to manually review employees who are potentially overpaid or underpaid.

An employee is considered to be potentially overpaid if they earn more than 2 times the average salary for people with the same title. Similarly, an employee might be underpaid if they earn less than half of the average for their title. We'll refer to employees who are both underpaid and overpaid as compensation outliers for the purposes of this problem.

Write a query that shows the following data for each compensation outlier: employee ID, salary, and whether they are potentially overpaid or potentially underpaid. [[Full Description](https://datalemur.com/questions/compensation-outliers)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT
    title
    ,AVG(salary) AS avg_pay
  FROM employee_pay
  GROUP BY title
)
SELECT
  p.employee_id
  ,p.salary
  ,CASE 
    WHEN c.avg_pay * 2 < p.salary THEN 'Overpaid' 
    WHEN c.avg_pay / 2 > p.salary THEN 'Underpaid'
    END AS status
FROM employee_pay AS p
JOIN cte AS c ON p.title = c.title
WHERE p.salary < c.avg_pay / 2 OR p.salary > c.avg_pay * 2
;
```

## Site Solution

```sql
-- DataLemur Solution 
WITH payout AS (
SELECT
  employee_id,
  salary,
  title,
  (AVG(salary) OVER (PARTITION BY title)) * 2 AS double_average,
  (AVG(salary) OVER (PARTITION BY title)) / 2 AS half_average
FROM employee_pay)

SELECT
  employee_id,
  salary,
  CASE WHEN salary > double_average THEN 'Overpaid'
    WHEN salary < half_average THEN 'Underpaid'
  END AS outlier_status
FROM payout
WHERE salary > double_average
  OR salary < half_average;
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
