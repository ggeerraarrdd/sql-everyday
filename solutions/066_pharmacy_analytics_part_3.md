# SQL Everyday \#066

## Pharmacy Analytics (Part 3)

Site: DataLemur\
Difficulty per Site: Easy

## Problem

CVS Health wants to gain a clearer understanding of its pharmacy sales and the performance of various products.

Write a query to calculate the total drug sales for each manufacturer. Round the answer to the nearest million and report your results in descending order of total sales. In case of any duplicates, sort them alphabetically by the manufacturer name.

Since this data will be displayed on a dashboard viewed by business stakeholders, please format your results as follows: "$36 million". [[Full Description](https://datalemur.com/questions/total-drugs-sales)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT 
  manufacturer
  ,CONCAT('$', ROUND(SUM(total_sales) / 1000000, 0), ' million') AS sales_mil
FROM pharmacy_sales
GROUP BY manufacturer
ORDER BY SUM(total_sales) DESC, manufacturer ASC
; 
```

## Site Solution

```sql
-- DataLemur Solution 
-- Site solution is essentially the same.
```

## Notes

TODO

## NB

TBD

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
