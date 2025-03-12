# SQL Everyday \#166

## Films selection with a twist

Site: Codewars\
Difficulty per Site: Medium

## Problem

For this task we need to get film_id, film title and length from the `film` table in the DVD rental database, but with a twist: we need to exclude films with a length between the minimum length of R-rated films and the median length of `PG-13` rated films. This means that the selected films will be either strictly shorter than the shortest R-rated film or strictly longer than of median length `PG-13` rated film [[Full Description](https://www.codewars.com/kata/644424f8d7bab510f1375d20)]

## Submitted Solution

```sql
-- Submitted Solution
WITH min_len AS (
  SELECT 
    MIN(length) AS min_length 
  FROM film 
  WHERE rating = 'R'
),
median_len AS (
  SELECT 
    PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY length) AS median_length
  FROM film
  WHERE rating = 'PG-13'
)
SELECT
  film_id
  ,title
  ,length
FROM film
WHERE (length < (SELECT min_length FROM min_len)) OR
  (length > (SELECT median_length FROM median_len))
ORDER BY length ASC, title ASC, film_id ASC
;
```

## Site Solution

```sql
-- Codewars Solution 
-- TBD
```

## Notes

TBD

## NB

`PERCENTILE_DISC`

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
