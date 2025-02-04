# SQL Everyday \#076

## Average Deal Size (Part 2)

Site: DataLemur\
Difficulty per Site: Medium

## Problem

Assuming Salesforce operates on a per user (per seat) pricing model, we have a table containing contracts data.

Write a query to calculate the average annual revenue per Salesforce customer in three market segments: SMB, Mid-Market, and Enterprise. Each customer is represented by a single contract. Format the output to match the structure shown in the Example Output section below [[Full Description](https://datalemur.com/questions/sql-average-deal-size-2)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
  SELECT
    co.customer_id
    ,SUM(co.num_seats * co.yearly_seat_cost) AS revenue
  FROM contracts AS co
  GROUP BY co.customer_id
),
cte2 AS (
SELECT
  c.customer_id
  ,c.revenue
  ,CASE 
    WHEN cu.employee_count < 100 THEN 'smb'
    WHEN cu.employee_count < 1000 THEN 'mid'
    ELSE 'enterprise' END AS market
FROM cte1 AS c
RIGHT JOIN customers AS cu ON c.customer_id = cu.customer_id
)
SELECT
  FLOOR(AVG(revenue) FILTER (WHERE market = 'smb'))::INT  AS smb_avg_revenue
  ,FLOOR(AVG(revenue) FILTER (WHERE market = 'mid'))::INT  AS mid_avg_revenue
  ,FLOOR(AVG(revenue) FILTER (WHERE market = 'enterprise'))::INT  AS enterprise_avg_revenue
FROM cte2
;
```

## Site Solution

```sql
-- DataLemur Solution 
WITH segment_cte AS (
  SELECT
    customer_id,
    CASE
      WHEN employee_count < 100 THEN 'smb'
      WHEN employee_count BETWEEN 100 AND 999 THEN 'mid'
      ELSE 'enterprise'
    END AS segment
  FROM customers
)
, revenue_cte AS (
  SELECT
    seg.segment,
    SUM(contracts.num_seats * contracts.yearly_seat_cost) 
      / COUNT(DISTINCT seg.customer_id) AS avg_revenue
  FROM segment_cte AS seg
  INNER JOIN contracts 
    ON seg.customer_id = contracts.customer_id
  GROUP BY seg.segment
)

SELECT
  SUM(CASE WHEN segment = 'smb' THEN avg_revenue END) AS smb_avg_revenue,
  SUM(CASE WHEN segment = 'mid' THEN avg_revenue END) AS mid_avg_revenue,
  SUM(CASE WHEN segment = 'enterprise' THEN avg_revenue END) AS enterprise_avg_revenue
FROM revenue_cte;
```

## Notes

TODO

## NB

TBD

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
