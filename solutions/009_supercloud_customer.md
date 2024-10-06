# SQL Everyday \#009

## Supercloud Customer

Site: DataLemur\
Difficulty per Site: Medium

## Problem

A Microsoft Azure Supercloud customer is defined as a customer who has purchased at least one product from every product category listed in the products table. Write a query that identifies the customer IDs of these Supercloud customers. [[Full Description](https://datalemur.com/questions/supercloud-customer)]

## Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT 
    customer_id
    ,product_category
    ,DENSE_RANK() OVER (PARTITION BY customer_id ORDER BY product_category) AS ranking
  FROM customer_contracts AS cc 
  JOIN products AS p ON cc.product_id = p.product_id
)
SELECT
  customer_id
FROM cte 
WHERE ranking = (SELECT COUNT(DISTINCT product_category) FROM products)
;
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
