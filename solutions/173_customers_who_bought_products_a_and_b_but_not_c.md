# SQL Everyday \#173

## Customers Who Bought Products A and B but Not C

Site: LeetCode\
Difficulty per Site: Medium

## Problem

Write a solution to report the customer_id and customer_name of customers who bought products *"A"*, *"B"* but did not buy the product *"C"* since we want to recommend them to purchase this product.

Return the result table *ordered* by `customer_id`. [[Full Description](https://leetcode.com/problems/customers-who-bought-products-a-and-b-but-not-c/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
    SELECT
        customer_id
        ,STRING_AGG(product_name, ',') AS products
    FROM Orders
    GROUP BY customer_id
)
SELECT
    c.customer_id
    ,c.customer_name
FROM Customers AS c
LEFT JOIN cte ON c.customer_id = cte.customer_id
WHERE (cte.products LIKE '%A%' 
    AND cte.products LIKE '%B%'
    AND cte.products NOT LIKE '%C%')
ORDER BY c.customer_id
;
```

## Site Solution

```sql
-- LeetCode Solution 
SELECT c.customer_id, customer_name
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id
HAVING SUM(product_name='A') > 0
    AND SUM(product_name='B') > 0
    AND SUM(product_name='C') = 0
ORDER BY c.customer_id;
```

## Notes

TBD

## NB

`STRING_AGG`

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
