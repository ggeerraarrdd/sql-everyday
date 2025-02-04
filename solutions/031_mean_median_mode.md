# SQL Everyday \#031

## Mean, Median, Mode

Site: DataLemur\
Difficulty per Site: Medium

## Problem

You're given a list of numbers representing the number of emails in the inbox of Microsoft Outlook users. Before the Product Management team can start developing features related to bulk-deleting email or achieving inbox zero, they simply want to find the mean, median, and mode for the emails.

Display the output of mean, median and mode (in this order), with the mean rounded to the nearest integer. It should be assumed that there are no ties for the mode. [[Full Description](https://datalemur.com/questions/mean-median-mode)]

## Submitted Solution

```sql
-- Submitted Solution
WITH mean AS (
SELECT
  ROUND(AVG(email_count)) AS mean
FROM inbox_stats
),
median AS (
SELECT
  PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY email_count) AS median
FROM inbox_stats
),
mode AS (
SELECT
  MODE() WITHIN GROUP (ORDER BY email_count) AS mode
FROM inbox_stats
)
SELECT
  (SELECT mean FROM mean) AS mean
  ,(SELECT median FROM median) AS median
  ,(SELECT mode FROM mode) AS mode
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT 
  ROUND(AVG(email_count)) as mean,
  PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY email_count) AS median,
  MODE() WITHIN GROUP (ORDER BY email_count) AS mode
  FROM inbox_stats;
```

## Notes

TODO

## NB

TBD

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
