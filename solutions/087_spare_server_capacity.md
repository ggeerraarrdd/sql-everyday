# SQL Everyday \#087

## Spare Server Capacity

Site: DataLemur\
Difficulty per Site: Easy

## Problem

Microsoft Azure's capacity planning team wants to understand how much data its customers are using, and how much spare capacity is left in each of its data centers. You’re given three tables: customers, data centers, and forecasted_demand.

Write a query to find each data centre’s total unused server capacity. Output the data center id in ascending order and the total spare capacity. [[Full Description](https://datalemur.com/questions/sql-spare-server-capacity)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT
    datacenter_id
    ,SUM(monthly_demand) AS monthly_demand
  FROM forecasted_demand
  GROUP BY datacenter_id
)
SELECT
  d.datacenter_id
  ,d.monthly_capacity - c.monthly_demand AS spare_capacity
FROM cte AS c 
JOIN datacenters AS d ON c.datacenter_id = d.datacenter_id
ORDER BY d.datacenter_id ASC
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT 
  centers.datacenter_id, 
  centers.monthly_capacity - SUM(demands.monthly_demand) AS spare_capacity
FROM forecasted_demand AS demands
INNER JOIN datacenters AS centers
  ON demands.datacenter_id = centers.datacenter_id
GROUP BY centers.datacenter_id, centers.monthly_capacity
ORDER BY centers.datacenter_id;
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
