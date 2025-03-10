# SQL Everyday \#164

## Even or Odd

Site: Codewars\
Difficulty per Site: Easy

## Problem

You will be given a table `numbers`, with one column `number`.

Return a dataset with two columns: `number` and `is_even`, where `number` contains the original input value, and `is_even` containing `"Even"` or `"Odd"` depending on number column values. [[Full Description](https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/sql)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
  number
  ,CASE WHEN number % 2 = 0 THEN 'Even' ELSE 'Odd' END AS is_even
 FROM numbers
 ;
```

## Site Solution

```sql
-- Codewars Solution 
-- TBD
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
