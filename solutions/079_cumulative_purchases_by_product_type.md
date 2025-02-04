# SQL Everyday \#079

## Cumulative Purchases by Product Type

Site: DataLemur\
Difficulty per Site: Medium

## Problem

Assume you're given a table containing Amazon purchasing activity. Write a query to calculate the cumulative purchases for each product type, ordered chronologically.

The output should consist of the order date, product, and the cumulative sum of quantities purchased. [[Full Description](https://datalemur.com/questions/sql-purchasing-activity)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
  order_date
  ,product_type
  ,SUM(quantity) OVER (PARTITION BY product_type ORDER BY order_date ASC) AS cum_purchased
FROM total_trans
ORDER BY order_date ASC
;
```

## Site Solution

```sql
-- DataLemur Solution 
-- Site solution essentially the same.
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
