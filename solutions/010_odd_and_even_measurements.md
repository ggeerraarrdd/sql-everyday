# SQL Everyday \#010

## Odd and Even Measurements

Site: DataLemur\
Difficulty per Site: Medium

## Problem

Assume you're given a table with measurement values obtained from a Google sensor over multiple days with measurements taken multiple times within each day.

Write a query to calculate the sum of odd-numbered and even-numbered measurements separately for a particular day and display the results in two different columns. Refer to the Example Output below for the desired format.

Definition:

Within a day, measurements taken at 1st, 3rd, and 5th times are considered odd-numbered measurements, and measurements taken at 2nd, 4th, and 6th times are considered even-numbered measurements. [[Full Description](https://datalemur.com/questions/odd-even-measurements)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
  SELECT 
    DATE_TRUNC('day', measurement_time) AS time_day
    ,measurement_value
    ,ROW_NUMBER() OVER (PARTITION BY DATE_TRUNC('day', measurement_time) ORDER BY measurement_time) AS row_num
  FROM measurements
),
cte2 AS (
  SELECT
    time_day
    ,CASE WHEN MOD(row_num, 2) = 0 THEN 0 ELSE measurement_value END odd_value
    ,CASE WHEN MOD(row_num, 2) = 0 THEN measurement_value ELSE 0 END even_value
  FROM cte1
)
SELECT
  time_day AS measurement_day
  ,SUM(odd_value) AS odd_sum
  ,SUM(even_value) AS even_sum
FROM cte2
GROUP BY time_day
ORDER BY time_day
;
```

## Site Solution

```sql
-- DataLemur Solution
WITH ranked_measurements AS (
  SELECT 
    CAST(measurement_time AS DATE) AS measurement_day, 
    measurement_value, 
    ROW_NUMBER() OVER (
      PARTITION BY CAST(measurement_time AS DATE) 
      ORDER BY measurement_time) AS measurement_num 
  FROM measurements
) 
SELECT 
  measurement_day, 
  SUM(measurement_value) FILTER (WHERE measurement_num % 2 != 0) AS odd_sum, 
  SUM(measurement_value) FILTER (WHERE measurement_num % 2 = 0) AS even_sum 
FROM ranked_measurements
GROUP BY measurement_day;
```

## Notes

* One difference between my submitted solution and DataLemur's is the use of `DATE_TRUNC()` vs `CAST()` in the `PARTITION BY` clause of window function.
* DataLemur was able to use one less CTE by using `FILTER`.
* Another difference is the use of `MOD()` vs a `%` arithmatic operator.

## NB

`MOD()`

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
