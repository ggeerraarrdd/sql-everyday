# SQL Everyday \#135

## Investments in 2016

Site: LeetCode\
Difficulty per Site: Medium

## Problem

Write a solution to report the sum of all total investment values in 2016 `tiv_2016`, for all policyholders who:

* have the same `tiv_2015` value as one or more other policyholders, and
* are not located in the same city as any other policyholder (i.e., the (`lat`, `lon`) attribute pairs must be unique).

Round `tiv_2016` to two decimal places. [[Full Description](https://leetcode.com/problems/investments-in-2016/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT 
    ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
    SELECT 
        tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
)
AND (lat, lon) IN (
    SELECT 
        lat
        ,lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
)
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



Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)

