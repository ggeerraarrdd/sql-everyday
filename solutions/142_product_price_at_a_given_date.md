# SQL Everyday \#142

## Product Price at a Given Date

Site: LeetCode\
Difficulty per Site: Medium

## Problem

Write a solution to find the prices of all products on `2019-08-16`. Assume the price of all products before any change is `10`.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/product-price-at-a-given-date/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
    SELECT
        DISTINCT product_id
    FROM Products
),
cte2 AS (
    SELECT
        product_id
        ,MAX(change_date) AS change_date
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
)
SELECT
    p1.product_id
    ,COALESCE(p3.new_price, 10) AS price
FROM cte1 AS p1
LEFT JOIN cte2 AS p2 ON p1.product_id = p2.product_id
LEFT JOIN Products AS p3 ON p2.product_id = p3.product_id AND p2.change_date = p3.change_date
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- Solution #1: Divide cases by using `UNION ALL`
SELECT
  product_id,
  10 AS price
FROM
  Products
GROUP BY
  product_id
HAVING
  MIN(change_date) > '2019-08-16'
UNION ALL
SELECT
  product_id,
  new_price AS price
FROM
  Products
WHERE
  (product_id, change_date) IN (
    SELECT
      product_id,
      MAX(change_date)
    FROM
      Products
    WHERE
      change_date <= '2019-08-16'
    GROUP BY
      product_id
  )

-- Solution #2: Divide cases by using `LEFT JOIN`
SELECT
  UniqueProductId.product_id,
  IFNULL (LastChangedPrice.new_price, 10) AS price
FROM
  (
    SELECT DISTINCT
      product_id
    FROM
      Products
  ) AS UniqueProductIds
  LEFT JOIN (
    SELECT
      Products.product_id,
      new_price
    FROM
      Products
      JOIN (
        SELECT
          product_id,
          MAX(change_date) AS change_date
        FROM
          Products
        WHERE
          change_date <= "2019-08-16"
        GROUP BY
          product_id
      ) AS LastChangedDate USING (product_id, change_date)
    GROUP BY
      product_id
  ) AS LastChangedPrice USING (product_id)

-- Solution #3: Use the window function
SELECT
  product_id,
  IFNULL (price, 10) AS price
FROM
  (
    SELECT DISTINCT
      product_id
    FROM
      Products
  ) AS UniqueProducts
  LEFT JOIN (
    SELECT DISTINCT
      product_id,
      FIRST_VALUE (new_price) OVER (
        PARTITION BY
          product_id
        ORDER BY
          change_date DESC
      ) AS price
    FROM
      Products
    WHERE
      change_date <= '2019-08-16'
  ) AS LastChangedPrice USING (product_id);
```

## Notes

TBD

## NB

`UNION ALL`, `LEFT JOIN`, Window Function

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
