# SQL Everyday \#084

## Highest Number of Products

Site: DataLemur\
Difficulty per Site: Easy

## Problem

Assume that you are given the table below containing information on various orders made by eBay customers. Write a query to obtain the user IDs and number of products purchased by the top 3 customers; these customers must have spent at least $1,000 in total.

Output the user id and number of products in descending order. To break ties (i.e., if 2 customers both bought 10 products), the user who spent more should take precedence. [[Full Description](https://datalemur.com/questions/sql-highest-products)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
  user_id
  ,COUNT(product_id) AS product_num
FROM user_transactions
GROUP BY user_id
HAVING SUM(spend) >= 1000
ORDER BY product_num DESC, SUM(spend) DESC
LIMIT 3
;
```

## Site Solution

```sql
-- DataLemur Solution 
-- Site solution essentially the same.
```

## Notes

* Aggregation in `ORDER BY` is allowed.

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
