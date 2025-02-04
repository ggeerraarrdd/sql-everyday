# SQL Everyday \#042

## QuickBooks vs TurboTax

Site: DataLemur\
Difficulty per Site: Easy

## Problem

Intuit provides a range of tax filing products, including TurboTax and QuickBooks, available in various versions.

Write a query to determine the total number of tax filings made using TurboTax and QuickBooks. Each user can file taxes once a year using only one product. [[Full Description](https://datalemur.com/questions/quickbooks-vs-turbotax)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
  COUNT(product) FILTER (WHERE LOWER(product) LIKE '%turbotax%') AS turbotax_total
  ,COUNT(product) FILTER (WHERE LOWER(product) LIKE '%quickbooks%') AS quickbooks_total
FROM filed_taxes
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT
  SUM (CASE WHEN LOWER(product) LIKE 'turbotax%' THEN 1 ELSE 0 END) AS turbotax_total,
  SUM (CASE WHEN LOWER(product) LIKE 'quickbooks%' THEN 1 ELSE 0 END) AS quickbooks_total
FROM filed_taxes;
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
