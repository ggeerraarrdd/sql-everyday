# SQL Everyday \#060

## Pharmacy Analytics (Part 1)

Site: DataLemur\
Difficulty per Site: Easy

## Problem

CVS Health is trying to better understand its pharmacy sales, and how well different products are selling. Each drug can only be produced by one manufacturer.

Write a query to find the top 3 most profitable drugs sold, and how much profit they made. Assume that there are no ties in the profits. Display the result from the highest to the lowest total profit. [[Full Description](https://datalemur.com/questions/top-profitable-drugs)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
  drug
  ,total_sales - cogs AS total_profit
FROM pharmacy_sales
ORDER BY total_profit DESC
LIMIT 3
;
```

## Site Solution

```sql
-- DataLemur Solution 
-- Site solution is essentially the same.
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
