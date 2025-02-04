# SQL Everyday \#024

## Unfinished Parts

Site: DataLemur\
Difficulty per Site: Easy

## Problem

Tesla is investigating production bottlenecks and they need your help to extract the relevant data. Write a query to determine which parts have begun the assembly process but are not yet finished.

This question is straightforward, so let's approach it with simplicity in both thinking and solution. [[Full Description](https://datalemur.com/questions/tesla-unfinished-parts)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
  part 
  ,assembly_step
FROM parts_assembly
WHERE finish_date IS NULL
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT part, assembly_step
FROM parts_assembly
WHERE finish_date IS NULL;
```

## Notes

TODO

## NB

TBD

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
