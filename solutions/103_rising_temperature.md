# SQL Everyday \#103

## Rising Temperature

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to find all dates' `id` with higher temperatures compared to its previous dates (yesterday).

Return the resulting table in *any order*. [[Full Description](https://leetcode.com/problems/rising-temperature/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    w1.id 
FROM Weather AS w1
LEFT JOIN Weather AS w2 
    ON DATE(w1.recordDate) = DATE(w2.recordDate + INTERVAL 1 DAY)
WHERE w1.temperature > w2.temperature
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- Approach 1: Using `JOIN` and `DATEDIFF()`
SELECT 
    w1.id
FROM 
    Weather w1
JOIN 
    Weather w2
ON 
    DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE 
    w1.temperature > w2.temperature;

-- Approach 2: Using `LAG()` Function
WITH PreviousWeatherData AS
(
    SELECT 
        id,
        recordDate,
        temperature, 
        LAG(temperature, 1) OVER (ORDER BY recordDate) AS PreviousTemperature,
        LAG(recordDate, 1) OVER (ORDER BY recordDate) AS PreviousRecordDate
    FROM 
        Weather
)
SELECT 
    id 
FROM 
    PreviousWeatherData
WHERE 
    temperature > PreviousTemperature
AND 
    recordDate = DATE_ADD(PreviousRecordDate, INTERVAL 1 DAY);

-- Approach 3: Using Subquery
SELECT 
    w1.id
FROM 
    Weather w1
WHERE 
    w1.temperature > (
        SELECT 
            w2.temperature
        FROM 
            Weather w2
        WHERE 
            w2.recordDate = DATE_SUB(w1.recordDate, INTERVAL 1 DAY)
    );

-- Approach 4: Using Cartesian Product and `WHERE` Clause
SELECT 
    w2.id
FROM 
    Weather w1, Weather w2
WHERE 
    DATEDIFF(w2.recordDate, w1.recordDate) = 1 
AND 
    w2.temperature > w1.temperature;
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
