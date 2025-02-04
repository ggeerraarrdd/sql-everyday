# SQL Everyday \#075

## ApplePay Volume

Site: DataLemur\
Difficulty per Site: Easy

## Problem

Visa is analysing its partnership with ApplyPay. Calculate the total transaction volume for each merchant where the transaction was performed via ApplePay.

Output the merchant ID and the total transactions. For merchants with no ApplePay transactions, output their total transaction volume as 0. Display the result in descending order of the transaction volume. [[Full Description](https://datalemur.com/questions/apple-pay-volume)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
  merchant_id
  ,SUM(CASE WHEN LOWER(payment_method) = 'apple pay' THEN transaction_amount ELSE 0 END) AS total_transaction
FROM transactions
GROUP BY merchant_id
ORDER BY total_transaction DESC
;
```

## Site Solution

```sql
-- DataLemur Solution 
-- Site solution essentially the same.
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
