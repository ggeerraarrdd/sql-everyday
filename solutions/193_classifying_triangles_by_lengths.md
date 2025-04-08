# SQL Everyday \#193

## Classifying Triangles by Lengths

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a query to find the type of **triangle**. Output one of the following for each row:

**Equilateral**: It's a triangle with 3 sides of equal length.
**Isosceles**: It's a triangle with 2 sides of equal length.
**Scalene**: It's a triangle with 3 sides of differing lengths.
**Not A Triangle**: The given values of A, B, and C don't form a triangle.

Return the result table in **any order**. [[Full Description](https://leetcode.com/problems/classifying-triangles-by-lengths/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    CASE WHEN (A=B AND A=C) THEN 'Equilateral'
    WHEN (A+B<=C OR B+C<=A OR A+C<=B) THEN 'Not A Triangle'
    WHEN (A=B AND A!=C) OR (A=C AND A!=B) OR(B=C AND A!=C) THEN 'Isosceles'
    ELSE 'Scalene'
    END AS 'triangle_type' 
FROM Triangles
;
```

## Site Solution

```sql
-- LeetCode Solution 
SELECT
    CASE WHEN (A=B AND A=C) THEN 'Equilateral'
        WHEN (A+B<=C OR B+C<=A OR A+C<=B) THEN 'Not A Triangle'
        WHEN (A=B AND A!=C) OR (A=C AND A!=B) OR(B=C AND A!=C) THEN 'Isosceles'
        ELSE 'Scalene'
        END AS 'triangle_type' 
FROM Triangles
;
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
