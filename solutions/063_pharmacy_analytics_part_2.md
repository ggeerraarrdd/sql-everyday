# SQL Everyday \#063

## Pharmacy Analytics (Part 2)

Site: DataLemur\
Difficulty per Site: Easy

## Problem

CVS Health is analyzing its pharmacy sales data, and how well different products are selling in the market. Each drug is exclusively manufactured by a single manufacturer.

Write a query to identify the manufacturers associated with the drugs that resulted in losses for CVS Health and calculate the total amount of losses incurred.

Output the manufacturer's name, the number of drugs associated with losses, and the total losses in absolute value. Display the results sorted in descending order with the highest losses displayed at the top. [[Full Description](https://datalemur.com/questions/non-profitable-drugs)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT 
    manufacturer
    ,product_id
    ,cogs - total_sales AS loss
  FROM pharmacy_sales
)
SELECT
  manufacturer
  ,COUNT(DISTINCT product_id) AS drug_count
  ,SUM(loss) AS total_loss
FROM cte
WHERE loss > 0
GROUP BY manufacturer
ORDER BY total_loss DESC
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT
  manufacturer,
  COUNT(drug) AS drug_count, 
  SUM(cogs - total_sales) AS total_loss
FROM pharmacy_sales
WHERE cogs > total_sales
GROUP BY manufacturer
ORDER BY total_loss DESC;
```

## Notes

* Had I realized `WHERE cogs > total_sales` would have filtered out drugs that were profitable, I would not have needed a CTE.

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
