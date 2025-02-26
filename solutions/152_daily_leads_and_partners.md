# SQL Everyday \#152

## Daily Leads and Partners

Site: LeetCode\
Difficulty per Site: Easy

## Problem

For each `date_id` and `make_name`, find the number of *distinct* `lead_id`'s and *distinct* `partner_id`'s.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/daily-leads-and-partners/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    date_id
    ,make_name
    ,COUNT(DISTINCT lead_id) AS unique_leads
    ,COUNT(DISTINCT partner_id) AS unique_partners
FROM DailySales
GROUP BY date_id, make_name
ORDER BY date_id ASC, make_name ASC
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- TBD
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
