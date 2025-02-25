# SQL Everyday \#151

## Capital Gain/Loss

Site: LeetCode\
Difficulty per Site: Medium

## Problem

Write a solution to report the *Capital gain/loss* for each stock.

The *Capital gain/loss* of a stock is the total gain or loss after buying and selling the stock one or many times.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/capital-gainloss/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
    SELECT
        stock_name
        ,CASE WHEN operation = 'Buy' THEN -price ELSE price END AS new_price
    FROM Stocks
)
SELECT
    stock_name
    ,SUM(new_price) AS capital_gain_loss
FROM cte
GROUP BY stock_name
;
```

## Site Solution

```sql
-- LeetCode Solution 
SELECT 
    stock_name,
    SUM(
        CASE 
            WHEN operation = 'buy' THEN -price
            WHEN operation = 'sell' THEN price
        END
    ) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
