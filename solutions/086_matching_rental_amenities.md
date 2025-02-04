# SQL Everyday \#086

## Matching Rental Amenities

Site: DataLemur\
Difficulty per Site: Hard

## Problem

The Airbnb Booking Recommendations team is trying to understand the "substitutability" of two rentals and whether one rental is a good substitute for another. They want you to write a query to find the unique combination of two Airbnb rentals with the same exact amenities offered.

Output the count of the unique combination of Airbnb rentals.

Assumptions:

* If property 1 has a kitchen and pool, and property 2 has a kitchen and pool too, it is a good substitute and represents a unique matching rental.
* If property 3 has a kitchen, pool and fireplace, and property 4 only has a pool and fireplace, then it is not a good substitute. [[Full Description](https://datalemur.com/questions/matching-rental-amenities)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT 
    rental_id, 
    ARRAY_AGG(amenity ORDER BY amenity) as amenities
  FROM rental_amenities
  GROUP BY rental_id
)
SELECT 
  COUNT(*) AS matching_airbnb
FROM cte AS c1 
JOIN cte AS c2 ON c1.amenities = c2.amenities AND c1.rental_id < c2.rental_id
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

`ARRAY_AGG()`

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
