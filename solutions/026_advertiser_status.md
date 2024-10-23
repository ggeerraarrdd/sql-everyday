# SQL Everyday \#026

## Advertiser Status

Site: DataLemur\
Difficulty per Site: Hard

## Problem

You're provided with two tables: the `advertiser` table contains information about advertisers and their respective payment status, and the `daily_pay` table contains the current payment information for advertisers, and it only includes advertisers who have made payments.

Write a query to update the payment status of Facebook advertisers based on the information in the `daily_pay` table. The output should include the user ID and their current payment status, sorted by the user id. [[Full Description](https://datalemur.com/questions/updated-status)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT
    COALESCE(a.user_id, d.user_id) AS user_id
    ,a.status
    ,d.paid
  FROM advertiser AS a
  FULL JOIN daily_pay AS d ON a.user_id = d.user_id
  ORDER BY a.user_id ASC
)
SELECT
  user_id
  ,CASE 
    WHEN status IS NULL AND paid IS NOT NULL THEN 'NEW'
    WHEN status = 'NEW' AND paid IS NOT NULL THEN 'EXISTING' 
    WHEN status = 'NEW' AND paid IS NULL THEN 'CHURN'
    WHEN status = 'EXISTING' AND paid IS NOT NULL THEN 'EXISTING'
    WHEN status = 'EXISTING' AND paid IS NULL THEN 'CHURN'
    WHEN status = 'CHURN' AND paid IS NOT NULL THEN 'RESURRECT'
    WHEN status = 'CHURN' AND paid IS NULL THEN 'CHURN'
    WHEN status = 'RESURRECT' AND paid IS NOT NULL THEN 'EXISTING'
    WHEN status = 'RESURRECT' AND paid IS NULL THEN 'CHURN'
    END AS new_status
FROM cte
ORDER by user_id ASC
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT 
  COALESCE(advertiser.user_id, daily_pay.user_id) AS user_id,
  CASE 
    WHEN paid IS NULL THEN 'CHURN' 
    WHEN paid IS NOT NULL AND advertiser.status IN ('NEW','EXISTING','RESURRECT') THEN 'EXISTING'
    WHEN paid IS NOT NULL AND advertiser.status = 'CHURN' THEN 'RESURRECT'
    WHEN paid IS NOT NULL AND advertiser.status IS NULL THEN 'NEW'
  END AS new_status
FROM advertiser
FULL OUTER JOIN daily_pay
  ON advertiser.user_id = daily_pay.user_id
ORDER BY user_id;
```

## Notes

* Unlike DataLemur's solution, I opted to code each case separately for readability and maintability.

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
