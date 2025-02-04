# SQL Everyday \#057

## Compressed Mean

Site: DataLemur\
Difficulty per Site: Easy

## Problem

You're trying to find the mean number of items per order on Alibaba, rounded to 1 decimal place using tables which includes information on the count of items in each order (`item_count` table) and the corresponding number of orders for each item count (`order_occurrences` table). [[Full Description](https://datalemur.com/questions/alibaba-compressed-mean)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT 
  ROUND(SUM(item_count::decimal * order_occurrences) / SUM(order_occurrences), 1) AS mean 
FROM items_per_order
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

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
