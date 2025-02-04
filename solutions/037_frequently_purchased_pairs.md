# SQL Everyday \#037

## Frequently Purchased Pairs

Site: DataLemur\
Difficulty per Site: Medium

## Problem

Given the Walmart transaction and product tables, write a query to determine the count of unique product combinations that are purchased together in the same transaction, considering that there must be a minimum of two products in the transaction. Display the output in ascending order of the product combinations.

For instance, if there are two transactions where apples and bananas are bought together, and another transaction where bananas and soy milk are bought together, the total count of unique combinations would be 2. [[Full Description](https://datalemur.com/questions/frequently-purchased-pairs)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT
    transaction_id
  FROM transactions
  GROUP BY transaction_id
  HAVING COUNT(*) >= 2
)
SELECT
  DISTINCT ARRAY_AGG(product_id::text ORDER BY product_id) AS combination
FROM transactions
WHERE transaction_id IN (SELECT transaction_id FROM cte)
GROUP BY transaction_id
ORDER BY combination ASC
;
```

## Site Solution

```sql
-- DataLemur Solution 
WITH array_table AS (
  SELECT 
    transaction_id, 
    ARRAY_AGG(CAST(product_id AS TEXT) ORDER BY product_id) as combination
  FROM transactions
  GROUP BY transaction_id
)

SELECT DISTINCT combination
FROM array_table
WHERE ARRAY_LENGTH(combination, 1) > 1
ORDER BY combination;
```

## Notes

TODO

## NB

`ARRAY_AGG()`, `ARRAY_LENGTH()`

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
