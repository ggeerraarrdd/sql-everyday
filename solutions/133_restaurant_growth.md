# SQL Everyday \#133

## Restaurant Growth

Site: LeetCode\
Difficulty per Site: Medium

## Problem

You are the restaurant owner and you want to analyze a possible expansion (there will be at least one customer every day).

Compute the moving average of how much the customer paid in a seven days window (i.e., current day + 6 days before). `average_amount` should be *rounded to two decimal places*.

Return the result table ordered by `visited_on` *in ascending order*. [[Full Description](https://leetcode.com/problems/restaurant-growth/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
    SELECT
        visited_on
        ,SUM(total_daily) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount
        ,ROUND(AVG(total_daily) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS average_amount
    FROM 
        (
        SELECT
            visited_on
            ,SUM(amount) as total_daily
        FROM Customer
        GROUP BY visited_on
        ORDER BY visited_on ASC
        ) AS daily
)
SELECT
    *
FROM cte
WHERE visited_on >= DATE((SELECT MIN(visited_on) FROM Customer) + INTERVAL 6 DAY)
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- None
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)

