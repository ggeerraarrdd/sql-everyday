# SQL Everyday \#022

## Swapped Food Delivery

Site: DataLemur\
Difficulty per Site: Medium

## Problem

Zomato is a leading online food delivery service that connects users with various restaurants and cuisines, allowing them to browse menus, place orders, and get meals delivered to their doorsteps.

Recently, Zomato encountered an issue with their delivery system. Due to an error in the delivery driver instructions, each item's order was swapped with the item in the subsequent row. As a data analyst, you're asked to correct this swapping error and return the proper pairing of order ID and item.

If the last item has an odd order ID, it should remain as the last item in the corrected data. For example, if the last item is Order ID 7 Tandoori Chicken, then it should remain as Order ID 7 in the corrected data.

In the results, return the correct pairs of order IDs and items. [[Full Description](https://datalemur.com/questions/sql-swapped-food-delivery)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
  SELECT
    order_id
    ,CASE WHEN MOD(order_id, 2) = 0 THEN order_id - 1 ELSE order_id END AS group_num
    ,item
  FROM orders
),
cte2 AS (
  SELECT
    order_id
    ,group_num
    ,item
    ,ROW_NUMBER() OVER (PARTITION BY group_num ORDER BY order_id DESC) AS partition_num
    ,ROW_NUMBER() OVER (ORDER BY group_num ASC, order_id DESC) AS corrected_order_id
  FROM cte1
)
SELECT
  corrected_order_id
  ,item
FROM cte2
;
```

## Site Solution

```sql
-- DataLemur Solution 
WITH order_counts AS (
  SELECT COUNT(order_id) AS total_orders 
  FROM orders
)

SELECT
  CASE
    WHEN order_id % 2 != 0 AND order_id != total_orders THEN order_id + 1
    WHEN order_id % 2 != 0 AND order_id = total_orders THEN order_id
    ELSE order_id - 1
  END AS corrected_order_id,
  item
FROM orders
CROSS JOIN order_counts
ORDER BY corrected_order_id;
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
