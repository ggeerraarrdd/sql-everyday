# SQL Everyday \#168

## SQL Basics: Simple UNION ALL

Site: Codewars\
Difficulty per Site: Medium

## Problem

For this challenge you need to create a UNION statement, there are two tables `ussales` and `eusales` the parent company tracks each sale at its respective location in each table, you must all filter the sale price so it only returns rows with a sale greater than `50.00`. You have been tasked with combining that data for future analysis. Order by location (US before EU), then by id. [[Full Description](https://www.codewars.com/kata/58112f8004adbbdb500004fe/sql)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
  'US' AS location
  ,id
  ,name
  ,price
  ,card_name
  ,card_number
  ,transaction_date
FROM ussales
WHERE price > 50.00
UNION ALL
SELECT
  'EU' AS location
  ,id
  ,name
  ,price
  ,card_name
  ,card_number
  ,transaction_date
FROM eusales
WHERE price > 50.00
;
```

## Site Solution

```sql
-- Codewars Solution 
select *
  from (select 'US' as location,
               id,
               name,
               price,
               card_name,
               card_number,
               transaction_date
          from ussales
        union all
        select 'EU' as location,
               id,
               name,
               price,
               card_name,
               card_number,
               transaction_date
          from eusales
       ) s
 where s.price > 50
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
