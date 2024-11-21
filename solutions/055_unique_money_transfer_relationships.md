# SQL Everyday \#055

## Unique Money Transfer Relationships

Site: DataLemur\
Difficulty per Site: Medium

## Problem

You are given a table of PayPal payments showing the payer, the recipient, and the amount paid. A two-way unique relationship is established when two people send money back and forth. Write a query to find the number of two-way unique relationships in this data. [[Full Description](https://datalemur.com/questions/money-transfer-relationships)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
  SELECT 
    p1.payer_id AS payer1
    ,p1.recipient_id AS payer1_to_recipient
    ,p2.recipient_id AS recipient_to_payer1
  FROM payments AS p1 
  LEFT JOIN payments AS p2 ON p1.recipient_id = p2.payer_id
),
cte2 AS (
  SELECT
    DISTINCT payer1, payer1_to_recipient
  FROM cte1
  WHERE payer1 = recipient_to_payer1
),
cte3 AS (
  SELECT
    CASE WHEN payer1 < payer1_to_recipient THEN payer1 ELSE NULL END AS payer1
    ,CASE WHEN payer1 < payer1_to_recipient THEN payer1_to_recipient ELSE NULL END AS payer2
  FROM cte2
)
SELECT
  COUNT(*) AS unique_relationships
FROM cte3
WHERE payer1 IS NOT NULL
;
```

## Site Solution

```sql
-- DataLemur Solution 
WITH relationships AS (
SELECT payer_id, recipient_id
FROM payments
INTERSECT
SELECT recipient_id, payer_id
FROM payments)

SELECT COUNT(payer_id) / 2 AS unique_relationships
FROM relationships;
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
