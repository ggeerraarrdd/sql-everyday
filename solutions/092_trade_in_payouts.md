# SQL Everyday \#092

## Trade In Payouts

Site: DataLemur\
Difficulty per Site: Easy

## Problem

Apple has a trade-in program where their customers can return the old iPhone device to Apple and Apple gives the customers the trade-in value (known as payout) of the device in cash.

For each store, write a query of the total revenue from the trade-in. Order the result by the descending order. [[Full Description](https://datalemur.com/questions/trade-in-payouts)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
  t.store_id
  ,SUM(p.payout_amount) AS payout_total
FROM trade_in_transactions AS t 
JOIN trade_in_payouts AS p ON t.model_id = p.model_id
GROUP BY store_id
ORDER BY payout_total DESC
;
```

## Site Solution

```sql
-- DataLemur Solution 
-- Site solution essentially the same.
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
