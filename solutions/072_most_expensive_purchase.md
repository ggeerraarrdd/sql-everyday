# SQL Everyday \#072

## Most Expensive Purchase

Site: DataLemur\
Difficulty per Site: Easy

## Problem

Amazon is trying to identify their high-end customers. To do so, they first need your help to write a query that obtains the most expensive purchase made by each customer. Order the results by the most expensive purchase first. [[Full Description](https://datalemur.com/questions/most-expensive-purchase)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT
    customer_id
    ,purchase_amount
    ,ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY purchase_amount DESC) AS rownum
  FROM transactions
)
SELECT
  customer_id
  ,purchase_amount
FROM cte 
WHERE rownum = 1
ORDER BY purchase_amount DESC
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT 
  customer_id, 
  MAX(purchase_amount) AS most_expensive_purchase
FROM transactions
GROUP BY customer_id
ORDER BY most_expensive_purchase DESC;
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
