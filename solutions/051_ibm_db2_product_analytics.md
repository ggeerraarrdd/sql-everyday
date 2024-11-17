# SQL Everyday \#051

## IBM db2 Product Analytics

Site: DataLemur\
Difficulty per Site: Easy

## Problem

IBM is analyzing how their employees are utilizing the Db2 database by tracking the SQL queries executed by their employees. The objective is to generate data to populate a histogram that shows the number of unique queries run by employees during the third quarter of 2023 (July to September). Additionally, it should count the number of employees who did not run any queries during this period.

Display the number of unique queries as histogram categories, along with the count of employees who executed that number of unique queries. [[Full Description](https://datalemur.com/questions/sql-ibm-db2-product-analytics)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
  SELECT 
    employee_id
    ,COUNT(query_id) AS query_count
  FROM queries
  WHERE query_starttime BETWEEN '2023-07-01' AND '2023-10-01'
  GROUP BY employee_id
),
cte2 AS (
  SELECT
    e.employee_id
    ,COALESCE(query_count, 0) AS query_count
  FROM employees AS e
  LEFT JOIN cte1 AS c ON e.employee_id = c.employee_id
  ORDER BY query_count
)
SELECT
  query_count AS unique_queries
  ,COUNT(employee_id) AS employee_count
FROM cte2
GROUP BY query_count
ORDER BY query_count ASC
;
```

## Site Solution

```sql
-- DataLemur Solution 
WITH employee_queries AS (
  SELECT 
    e.employee_id,
    COALESCE(COUNT(DISTINCT q.query_id), 0) AS unique_queries
  FROM employees AS e
  LEFT JOIN queries AS q
    ON e.employee_id = q.employee_id
      AND q.query_starttime >= '2023-07-01T00:00:00Z'
      AND q.query_starttime < '2023-10-01T00:00:00Z'
  GROUP BY e.employee_id
)

SELECT
  unique_queries,
  COUNT(employee_id) AS employee_count
FROM employee_queries
GROUP BY unique_queries
ORDER BY unique_queries;
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
