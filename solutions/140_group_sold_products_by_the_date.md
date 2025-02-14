# SQL Everyday \#140

## Group Sold Products By The Date

Site: DataLemur\
Difficulty per Site: Easy

## Problem

Write a solution to find for each date the number of different products sold and their names.

The sold products names for each date should be sorted lexicographically.

Return the result table ordered by `sell_date`. [[Full Description](https://leetcode.com/problems/group-sold-products-by-the-date/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    sell_date
    ,COUNT(DISTINCT product) AS num_sold
    ,GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ",") AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date ASC, products ASC
;
```

## Site Solution

```sql
-- DataLemur Solution 
-- TBD
```

## Notes

TBD

## NB

`GROUP_CONCAT()`

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
