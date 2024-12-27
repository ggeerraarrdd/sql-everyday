# SQL Everyday \#091

## Product Line Revenue

Site: DataLemur\
Difficulty per Site: Easy

## Problem

As a business analyst on the revenue forecasting team at NVIDIA, you are given a table of NVIDIA transactions in 2021.

Write a query to summarize the total sales revenue for each product line. The product line with the highest revenue should be at the top of the results.

Assumption:

* There will be at least one sale of each product line. [[Full Description](https://datalemur.com/questions/revenue-by-product-line)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
  p.product_line
  ,SUM(amount) AS total_revenue
FROM transactions AS t
JOIN product_info AS p ON t.product_id = p.product_id
GROUP BY p.product_line
ORDER BY total_revenue DESC
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT
  DISTINCT product.product_line,
  SUM(amount) OVER (
    PARTITION BY product.product_line) AS total_revenue
FROM transactions
INNER JOIN product_info AS product
  ON transactions.product_id = product.product_id
ORDER BY total_revenue DESC;
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
