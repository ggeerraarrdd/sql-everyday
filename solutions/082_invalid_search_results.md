# SQL Everyday \#082

## Invalid Search Results

Site: DataLemur\
Difficulty per Site: Medium

## Problem

Assume you are given the table below containing the information on the searches attempted and the percentage of invalid searches by country. Write a query to obtain the percentage of invalid searches.

Output the country in ascending order, total searches and overall percentage of invalid searches rounded to 2 decimal places. [[Full Description](https://datalemur.com/questions/invalid-search-pct)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT
    country
    ,SUM(num_search) OVER (PARTITION BY country) AS total_search
    ,SUM(num_search * (invalid_result_pct / 100.0)) OVER(PARTITION BY country) AS invalid_searches
    ,ROW_NUMBER() OVER (PARTITION BY country) AS rownum
  FROM search_category
  WHERE invalid_result_pct IS NOT NULL
)
SELECT
  country
  ,total_search
  ,ROUND(100.0 * invalid_searches / total_search, 2) AS invalid_searches_pct
FROM cte
WHERE rownum = 1
  AND (total_search IS NOT NULL OR invalid_searches IS NOT NULL)
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT 
  country,
  SUM(num_search) AS total_searches,
  ROUND(SUM(num_search * invalid_result_pct)/SUM(num_search),2) AS invalid_searches_pct
FROM search_category
WHERE invalid_result_pct IS NOT NULL
GROUP BY country
ORDER BY country;
```

## Notes

TODO

## NB

TBD

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
