# SQL Everyday \#110

## Average Selling Price

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to find the average selling price for each product. average_price should be *rounded to 2 decimal places*. If a product does not have any sold units, its average selling price is assumed to be 0.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/average-selling-price/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS 
    (
    SELECT
        p.product_id AS product_id
        ,CASE WHEN s.purchase_date >= p.start_date AND s.purchase_date <= p.end_date THEN s.units ELSE 0 END AS units
        ,CASE WHEN s.purchase_date >= p.start_date AND s.purchase_date <= p.end_date THEN s.units * p.price ELSE 0 END AS price
    FROM Prices p
    LEFT JOIN UnitsSold s ON p.product_id = s.product_id
    )
SELECT
    product_id
    ,IFNULL(ROUND(SUM(price) / SUM(units), 2), 0) AS average_price
FROM cte
GROUP BY product_id
;
```

## Site Solution

```sql
-- LeetCode Solution 
SELECT
    p.product_id,
    IFNULL(ROUND(SUM(p.price * u.units) / SUM(u.units), 2), 0) AS average_price
FROM
    Prices AS p
LEFT JOIN
    UnitsSold AS u
ON
    p.product_id = u.product_id
    AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY
    p.product_id;
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
