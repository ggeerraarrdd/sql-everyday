# SQL Everyday \#094

## Who Made Quota?

Site: DataLemur\
Difficulty per Site: Easy

## Problem

As a data analyst on the Oracle Sales Operations team, you are given a list of salespeople’s deals, and the annual quota they need to hit.

Write a query that outputs each employee id and whether they hit the quota or not ('yes' or 'no'). Order the results by employee id in ascending order. [[Full Description](https://datalemur.com/questions/oracle-sales-quota)]

## Submitted Solution

```sql
-- Submitted Solution
WITH deals AS (
  SELECT
    employee_id
    ,SUM(deal_size) AS total_deals
  FROM deals
  GROUP BY employee_id
)
SELECT
  d.employee_id
  ,CASE WHEN d.total_deals >= q.quota THEN 'yes' ELSE 'no' END AS made_quota
FROM deals AS d 
JOIN sales_quotas AS q ON d.employee_id = q.employee_id
ORDER BY d.employee_id ASC
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT 
  deals.employee_id,
  CASE 
    WHEN SUM(deals.deal_size) > quotas.quota THEN 'yes' 
    ELSE 'no' 
  END AS made_quota
FROM deals
INNER JOIN sales_quotas AS quotas
  ON deals.employee_id = quotas.employee_id
GROUP BY deals.employee_id, quotas.quota
ORDER BY deals.employee_id;
```

## Notes

TODO

## NB

TBD

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
