# SQL Everyday \#200

## Shortest Distance in a Plane

Site: LeetCode\
Difficulty per Site: Medium

## Problem

The distance between two points `p1(x1, y1)` and `p2(x2, y2)` is `sqrt((x2 - x1)2 + (y2 - y1)2)`.

Write a solution to report the shortest distance between any two points from the `Point2D` table. Round the distance to **two decimal points**. [[Full Description](https://leetcode.com/problems/shortest-distance-in-a-plane/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
    SELECT
        -- p1.x AS x_1
        -- ,p1.y AS y_1
        -- ,p2.x AS x_2
        -- ,p2.y AS y_2
        ROUND(SQRT( (p2.x - p1.x)^2 + (p2.y - p1.y)^2 )::numeric, 2) AS distances
    FROM Point2D as p1
    CROSS JOIN Point2D AS p2
)
SELECT
    MIN(distances) AS shortest
FROM cte
WHERE distances > 0
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- Approach 1: Using SQRT, POW() functions and math knowledge
ELECT
    ROUND(SQRT(MIN((POW(p1.x - p2.x, 2) + POW(p1.y - p2.y, 2)))), 2) AS shortest
FROM
    point_2d p1
        JOIN
    point_2d p2 ON p1.x != p2.x OR p1.y != p2.y
;

-- Approach 2: Optimize to avoid reduplicate calculations
SELECT
    ROUND(SQRT(MIN((POW(p1.x - p2.x, 2) + POW(p1.y - p2.y, 2)))),2) AS shortest
FROM
    point_2d p1
        JOIN
    point_2d p2 ON (p1.x <= p2.x AND p1.y < p2.y)
        OR (p1.x <= p2.x AND p1.y > p2.y)
        OR (p1.x < p2.x AND p1.y = p2.y)
;
```

## Notes

TBD

## NB

`CROSS JOIN`

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
