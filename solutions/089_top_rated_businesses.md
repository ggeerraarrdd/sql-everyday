# SQL Everyday \#089

## Top Rated Businesses

Site: DataLemur\
Difficulty per Site: Easy

## Problem

Assume you are given the table below containing information on user reviews. Write a query to obtain the number and percentage of businesses that are top rated. A top-rated busines is defined as one whose reviews contain only 4 or 5 stars.

Output the number of businesses and percentage of top rated businesses rounded to the nearest integer.

Assumption:

* Each business has only one review (which is the business' average rating). [[Full Description](https://datalemur.com/questions/sql-top-businesses)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
  COUNT(*) FILTER (WHERE review_stars >= 4) AS business_count
  ,100 * COUNT(*) FILTER (WHERE review_stars >= 4) / COUNT(*) AS top_rated_pct
FROM reviews
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT 
  COUNT(business_id) AS business_count,
  ROUND(100.0 * COUNT(business_id)/
    (SELECT COUNT (business_id) FROM reviews),0) AS top_rated_pct
FROM reviews
WHERE review_stars IN (4, 5);
```

## Notes

TODO

## NB

TBD

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
