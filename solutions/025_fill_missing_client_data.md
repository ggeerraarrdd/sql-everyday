# SQL Everyday \#025

## Fill Missing Client Data

Site: DataLemur\
Difficulty per Site: Medium

## Problem

When accessing Accenture's retailer client's database, you observe that the category column in products table contains null values.

Write a query that returns the updated product table with all the category values filled in, taking into consideration the assumption that the first product in each category will always have a defined category value. [[Full Description](https://datalemur.com/questions/fill-missing-product)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT
    *
    ,COUNT(category) OVER (ORDER BY product_id) AS numbered_category
  FROM products
)
SELECT
  product_id
  ,FIRST_VALUE(category) OVER (PARTITION BY numbered_category) AS category
  ,name
FROM cte
;
```

## Site Solution

```sql
-- DataLemur Solution 
WITH filled_category AS (
SELECT
  *,
  COUNT(category) OVER (ORDER BY product_id) AS numbered_category
FROM products
)

SELECT
  product_id,
  COALESCE(category, MAX(category) OVER (PARTITION BY numbered_category)) AS category,
  name
FROM filled_category;
```

## Notes

* I had to check DataLemur's hint to solve this problem. Interesting use of `COUNT()` and window function for assigning new categories but could only work with the given assumption.

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
