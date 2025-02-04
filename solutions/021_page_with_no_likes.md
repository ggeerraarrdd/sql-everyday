# SQL Everyday \#021

## Page With No Likes

Site: DataLemur\
Difficulty per Site: Easy

## Problem

Assume you're given two tables containing data about Facebook Pages and their respective likes (as in "Like a Facebook Page").

Write a query to return the IDs of the Facebook pages that have zero likes. The output should be sorted in ascending order based on the page IDs. [[Full Description](https://datalemur.com/questions/sql-page-with-no-likes)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT p.page_id 
FROM pages AS p
LEFT JOIN page_likes AS pl ON p.page_id = pl.page_id
WHERE pl.user_id IS NULL
ORDER BY p.page_id ASC
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT page_id
FROM pages
EXCEPT
SELECT page_id
FROM page_likes;
```

## Notes

TODO

## NB

TBD

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
