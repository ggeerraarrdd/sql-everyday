# SQL Everyday \#181

## Customer Order Frequency

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to report the `customer_id` and `customer_name` of customers who have spent at least `$100` in each month of **June and July 2020**.

Return the result table in **any order**. [[Full Description](https://leetcode.com/problems/customer-order-frequency/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
    SELECT
        c.customer_id
        ,c.name
        ,DATE_TRUNC('month', o.order_date) AS month
        ,SUM(o.quantity * p.price) AS total
    FROM Orders AS o
    JOIN Product AS p ON o.product_id = p.product_id
    JOIN Customers AS c ON o.customer_id = c.customer_id
    GROUP BY c.customer_id, c.name, month
),
cte2 AS (
    SELECT
        customer_id
        ,name
        ,SUM(CASE WHEN (month = '2020-06-01' or month = '2020-07-01') AND total >= 100 THEN 1
            ELSE 0 END) AS validation
    FROM cte1
    GROUP BY customer_id, name
)
SELECT
    customer_id
    ,name
FROM cte2
WHERE validation = 2
;
```

## Site Solution

```sql
-- LeetCode Solution 
SELECT 
  customer_id, 
  name 
FROM 
  Customers 
  JOIN Orders USING(customer_id) 
  JOIN Product USING(product_id) 
WHERE 
  YEAR(order_date)= 2020 
GROUP BY 
  customer_id 
HAVING 
  SUM(
      IF(MONTH(order_date) = 6, quantity, 0) * price
  ) >= 100 AND 
  SUM(
      IF(MONTH(order_date) = 7, quantity, 0) * price
  ) >= 100;
```

## Notes

TBD

## NB

`USING`, `HAVING`

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
