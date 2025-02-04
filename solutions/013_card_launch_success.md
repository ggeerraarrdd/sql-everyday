# SQL Everyday \#013

## Card Launch Success

Site: DataLemur\
Difficulty per Site: Medium

## Problem

Your team at JPMorgan Chase is soon launching a new credit card. You are asked to estimate how many cards you'll issue in the first month. Before you can answer this question, you want to first get some perspective on how well new credit card launches typically do in their first month. Write a query that outputs the name of the credit card, and how many cards were issued in its launch month. The launch month is the earliest record in the `monthly_cards_issued` table for a given card. Order the results starting from the biggest issued amount. [[Full Description](https://datalemur.com/questions/card-launch-success)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT 
    card_name
    ,issue_year
    ,issue_month
    ,issued_amount
    ,ROW_NUMBER() OVER (PARTITION BY card_name ORDER BY issue_year ASC, issue_month ASC) AS ranking
  FROM monthly_cards_issued
)
SELECT
  card_name
  ,issued_amount
FROM cte
WHERE ranking = 1
ORDER BY issued_amount DESC
;
```

## Site Solution

```sql
-- DataLemur Solution 
WITH card_launch AS (
  SELECT 
    card_name,
    issued_amount,
    MAKE_DATE(issue_year, issue_month, 1) AS issue_date,
    MIN(MAKE_DATE(issue_year, issue_month, 1)) OVER (
      PARTITION BY card_name) AS launch_date
  FROM monthly_cards_issued
)
SELECT 
  card_name, 
  issued_amount
FROM card_launch
WHERE issue_date = launch_date
ORDER BY issued_amount DESC;
```

## Notes

TODO

## NB

TBD

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
