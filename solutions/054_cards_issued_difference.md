# SQL Everyday \#054

## Cards Issued Difference

Site: DataLemur\
Difficulty per Site: Easy

## Problem

Your team at JPMorgan Chase is preparing to launch a new credit card, and to gain some insights, you're analyzing how many credit cards were issued each month.

Write a query that outputs the name of each credit card and the difference in the number of issued cards between the month with the highest issuance cards and the lowest issuance. Arrange the results based on the largest disparity. [[Full Description](https://datalemur.com/questions/cards-issued-difference)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT 
  card_name
  ,MAX(issued_amount) - MIN(issued_amount) AS difference 
FROM monthly_cards_issued
GROUP BY card_name
ORDER BY difference DESC
;
```

## Site Solution

```sql
-- DataLemur Solution 
-- Site solution is essentially the same.
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
