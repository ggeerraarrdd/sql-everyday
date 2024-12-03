# SQL Everyday \#067

## Photoshop Revenue Analysis

Site: DataLemur\
Difficulty per Site: Medium

## Problem

For every customer that bought Photoshop, return a list of the customers, and the total spent on all the products except for Photoshop products.

Sort your answer by customer ids in ascending order. [[Full Description](https://datalemur.com/questions/photoshop-revenue-analysis)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
  customer_id
  ,SUM(revenue) AS revenue
FROM adobe_transactions
WHERE customer_id IN (
  SELECT 
    customer_id 
  FROM adobe_transactions 
  WHERE LOWER(product) LIKE '%photoshop%'
  )
    AND LOWER(product) NOT LIKE '%photoshop%'
GROUP BY customer_id
ORDER BY customer_id ASC
;
```

## Site Solution

```sql
-- DataLemur Solution 
-- Solution #1
-- Site solution is essentially the same.

-- Solution #2: Using SELF JOIN
SELECT 
  original.customer_id,
  SUM(original.revenue) AS revenue
FROM adobe_transactions AS original
INNER JOIN adobe_transactions AS filtered
  ON original.customer_id = filtered.customer_id
  AND filtered.product = 'Photoshop'
WHERE original.product <> 'Photoshop'
GROUP BY original.customer_id
ORDER BY original.customer_id; 
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
