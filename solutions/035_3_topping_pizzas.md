# SQL Everyday \#035

## 3-Topping Pizzas

Site: DataLemur\
Difficulty per Site: Hard

## Problem

You’re a consultant for a major pizza chain that will be running a promotion where all 3-topping pizzas will be sold for a fixed price, and are trying to understand the costs involved.

Given a list of pizza toppings, consider all the possible 3-topping pizzas, and print out the total cost of those 3 toppings. Sort the results with the highest total cost on the top followed by pizza toppings in ascending order.

Break ties by listing the ingredients in alphabetical order, starting from the first ingredient, followed by the second and third. [[Full Description](https://datalemur.com/questions/pizzas-topping-cost)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
  SELECT
    p1.topping_name AS topping1
    ,p2.topping_name AS topping2
    ,p3.topping_name AS topping3
    ,p1.ingredient_cost + p2.ingredient_cost + p3.ingredient_cost AS total_cost
  FROM pizza_toppings p1
  CROSS JOIN pizza_toppings p2
  CROSS JOIN pizza_toppings p3
  WHERE p1.topping_name <> p2.topping_name
    AND p1.topping_name <> p3.topping_name
    AND p2.topping_name <> p3.topping_name
  ORDER by topping1, topping2, topping3
),
cte2 AS (
  SELECT
    CONCAT(
    LEAST(topping1, topping2, topping3), ',',
    CASE 
        WHEN topping1 < topping2 AND topping2 < topping3 THEN topping2
        WHEN topping1 < topping3 AND topping3 < topping2 THEN topping3
        WHEN topping2 < topping1 AND topping1 < topping3 THEN topping1
        WHEN topping2 < topping3 AND topping3 < topping1 THEN topping3
        WHEN topping3 < topping1 AND topping1 < topping2 THEN topping1
        ELSE topping2
    END, ',',
    GREATEST(topping1, topping2, topping3)
    ) AS pizza
    ,total_cost
  FROM cte1
)
SELECT
  DISTINCT pizza
  ,total_cost
FROM cte2
ORDER BY total_cost DESC, pizza ASC; 
```

## Site Solution

```sql
-- DataLemur Solution 
-- Solution #1: Using INNER JOIN
SELECT 
  CONCAT(p1.topping_name, ',', p2.topping_name, ',', p3.topping_name) AS pizza,
  p1.ingredient_cost + p2.ingredient_cost + p3.ingredient_cost AS total_cost
FROM pizza_toppings AS p1
INNER JOIN pizza_toppings AS p2
  ON p1.topping_name < p2.topping_name 
INNER JOIN pizza_toppings AS p3
  ON p2.topping_name < p3.topping_name 
ORDER BY total_cost DESC, pizza;

-- Solution #2: Using CROSS JOIN
SELECT 
  CONCAT(p1.topping_name, ',', p2.topping_name, ',', p3.topping_name) AS pizza,
  p1.ingredient_cost + p2.ingredient_cost + p3.ingredient_cost AS total_cost
FROM pizza_toppings AS p1
CROSS JOIN
  pizza_toppings AS p2,
  pizza_toppings AS p3
WHERE p1.topping_name < p2.topping_name
  AND p2.topping_name < p3.topping_name
ORDER BY total_cost DESC, pizza;

-- Solution #3: Using RECURSIVE CTE
WITH RECURSIVE all_toppings AS (
  SELECT
  topping_name::VARCHAR,
  ingredient_cost::DECIMAL AS total_cost,
  1 AS topping_numbers
FROM pizza_toppings

UNION ALL

SELECT
  CONCAT(addon.topping_name, ',', anchor.topping_name) AS topping_name,
  addon.ingredient_cost + anchor.total_cost AS total_cost,
  topping_numbers + 1
FROM 
  pizza_toppings AS addon, 
  all_toppings AS anchor
WHERE anchor.topping_name < addon.topping_name
)

SELECT
  STRING_AGG (single_topping, ',' ORDER BY single_topping) AS pizza,
  total_cost
FROM 
  all_toppings, 
  REGEXP_SPLIT_TO_TABLE(topping_name, ',') AS single_topping
WHERE topping_numbers = 3
GROUP BY topping_name, total_cost
ORDER BY total_cost DESC, pizza;

-- Solution #4: Using Array Function
WITH RECURSIVE all_toppings AS (
SELECT
  topping_name::VARCHAR,
  ingredient_cost::DECIMAL AS total_cost,
  1 AS topping_numbers
FROM pizza_toppings

UNION ALL

SELECT
  CONCAT(addon.topping_name, ',', anchor.topping_name) AS topping_name,
  addon.ingredient_cost + anchor.total_cost AS total_cost,
  topping_numbers + 1
FROM 
  pizza_toppings AS addon,
  all_toppings AS anchor
WHERE anchor.topping_name < addon.topping_name
), 
arrange AS (
SELECT
  topping_name,
  UNNEST(STRING_TO_ARRAY(topping_name, ',')) AS single_topping,
  total_cost
FROM all_toppings
WHERE topping_numbers = 3
)

SELECT
  STRING_AGG(single_topping, ',' ORDER BY single_topping) AS pizza,
  total_cost
FROM arrange
GROUP BY topping_name, total_cost
ORDER BY total_cost DESC, pizza;
```

## Notes

TODO

## NB

TBD

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
