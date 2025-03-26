# SQL Everyday \#180

## Books with NULL Ratings

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to find all books that have not been rated yet (i.e., have a **NULL** rating).

Return the result table ordered by `book_id` in **ascending** order. [[Full Description](https://leetcode.com/problems/books-with-null-ratings/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    book_id
    ,title
    ,author
    ,published_year
FROM books
WHERE rating IS NULL
ORDER BY book_id ASC
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
