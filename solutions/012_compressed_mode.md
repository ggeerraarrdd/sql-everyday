# SQL Everyday \#012

## Compressed Mode

Site: DataLemur\
Difficulty per Site: Medium

## Problem

You're given a table containing the item count for each order on Alibaba, along with the frequency of orders that have the same item count. Write a query to retrieve the mode of the order occurrences. Additionally, if there are multiple item counts with the same mode, the results should be sorted in ascending order. [[Full Description](https://datalemur.com/questions/alibaba-compressed-mode)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
  item_count
FROM items_per_order
WHERE order_occurrences = (SELECT MAX(order_occurrences) FROM items_per_order)
ORDER BY item_count ASC
;



```

## Site Solution

```sql
-- DataLemur Solution 1
-- Method #1: Using MAX()
SELECT item_count AS mode
FROM items_per_order
WHERE order_occurrences = (SELECT MAX(order_occurrences) FROM items_per_order
)
ORDER BY item_count;

-- Method #2: Using MODE() WITHIN GROUP ()
SELECT item_count AS mode
FROM items_per_order
WHERE order_occurrences = (SELECT MODE() WITHIN GROUP (ORDER BY order_occurrences DESC) FROM items_per_order
)
ORDER BY item_count;
```

## Notes

* DataLemur's 2nd solution made use of [`MODE()`](https://www.postgresql.org/docs/9.5/functions-aggregate.html) which is supported by PostgreSQL, its integrated database environment. But others such as MySQL have no such built-in function.

## NB

`MODE()`

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
