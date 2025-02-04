# SQL Everyday \#059

## Repeated Payments

Site: DataLemur\
Difficulty per Site: Hard

## Problem

Sometimes, payment transactions are repeated by accident; it could be due to user error, API failure or a retry error that causes a credit card to be charged twice.

Using the transactions table, identify any payments made at the same merchant with the same credit card for the same amount within 10 minutes of each other. Count such repeated payments. [[Full Description](https://datalemur.com/questions/repeated-payments)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
SELECT 
  *
  ,EXTRACT(EPOCH FROM transaction_timestamp - LAG(transaction_timestamp, 1) OVER (PARTITION BY merchant_id, credit_card_id, amount ORDER BY transaction_timestamp ASC))/60 AS lag
FROM transactions
)
SELECT
  COUNT(transaction_id) AS payment_count
FROM cte
WHERE lag <= 10
;
```

## Site Solution

```sql
-- DataLemur Solution 
-- Site solution is essentially the same.
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
