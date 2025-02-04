# SQL Everyday \#041

## Compressed Median

Site: DataLemur\
Difficulty per Site: Hard

## Problem

You are trying to find the median number of items bought per order on Alibaba, rounded to 1 decimal point.

However, instead of doing analytics on all Alibaba orders, you have access to a summary table, which describes how many items were in an order, and the number of orders that had that many items. [[Full Description](https://datalemur.com/questions/alibaba-compressed-median)]

## Submitted Solution

```sql
-- Submitted Solution
WITH expanded_data AS (
  SELECT 
    item_count
    ,GENERATE_SERIES(1, order_occurrences) AS series
  FROM items_per_order
)
SELECT
  ROUND(CAST(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY item_count DESC) AS DECIMAL), 1) AS median
FROM expanded_data
;
```

## Site Solution

```sql
-- DataLemur Solution 
WITH running_orders AS (
    SELECT
        *,
        SUM(order_occurrences) OVER (
            ORDER BY item_count ASC) as running_sum,
        SUM(order_occurrences) OVER () AS total_sum
    FROM items_per_order
)

SELECT ROUND(AVG(item_count),1) AS median
FROM running_orders
WHERE total_sum <= 2 * running_sum
    AND total_sum >= 2 * (running_sum - order_occurrences);
```

## Notes

TODO

## NB

`GENERATE_SERIES()`, `PERCENTILE_CONT()`

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
