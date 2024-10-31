# SQL Everyday \#034

## Pharmacy Analytics (Part 4)

Site: DataLemur\
Difficulty per Site: Medium

## Problem

CVS Health is trying to better understand its pharmacy sales, and how well different drugs are selling.

Write a query to find the top 2 drugs sold, in terms of units sold, for each manufacturer. List your results in alphabetical order by manufacturer. [[Full Description](https://datalemur.com/questions/top-drugs-sold)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT
    manufacturer
    ,drug
    ,ROW_NUMBER() OVER (PARTITION BY manufacturer ORDER BY units_sold DESC) AS drug_rank
  FROM pharmacy_sales
)
SELECT
  manufacturer
  ,drug
FROM cte
WHERE drug_rank <= 2
ORDER BY manufacturer ASC
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT
  manufacturer, drug
FROM (
  SELECT
    manufacturer,
    drug,
    ROW_NUMBER() OVER (
      PARTITION BY manufacturer
      ORDER BY units_sold DESC) AS drug_position
  FROM pharmacy_sales
) AS top_drugs
WHERE drug_position <= 2
ORDER BY manufacturer;
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
