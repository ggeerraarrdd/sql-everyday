# SQL Everyday \#167

## SQL Basics: Raise to the Power

Site: Codewars\
Difficulty per Site: Easy

## Problem

Return a table with a single column `result` which is the output of number1 raised to the power of number2. [[Full Description](https://www.codewars.com/kata/594a8f653b5b4e8f3d000035)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
  number1 ^ number2 AS result
FROM decimals
;
```

## Site Solution

```sql
-- Codewars Solution 
SELECT
  POW(NUMBER1, NUMBER2) AS RESULT
FROM
  DECIMALS
```

## Notes

TBD

## NB

`^` or `POW()`

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
