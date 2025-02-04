# SQL Everyday \#039

## Final Account Balance

Site: DataLemur\
Difficulty per Site: Easy

## Problem

Given a table containing information about bank deposits and withdrawals made using Paypal, write a query to retrieve the final account balance for each account, taking into account all the transactions recorded in the table with the assumption that there are no missing transactions. [[Full Description](https://datalemur.com/questions/final-account-balance)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
  account_id
  ,SUM(CASE WHEN transaction_type = 'Deposit' THEN amount ELSE -amount END) AS final_balance
FROM transactions
GROUP BY account_id
;
```

## Site Solution

```sql
-- DataLemur Solution 
-- Similar to submitted solution
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
