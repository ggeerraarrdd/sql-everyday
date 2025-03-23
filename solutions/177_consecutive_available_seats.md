# SQL Everyday \#177

## Consecutive Available Seats

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Find all the consecutive available seats in the cinema.

Return the result table **ordered** by `seat_id` **in ascending order**. [[Full Description](https://leetcode.com/problems/consecutive-available-seats/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
    SELECT
        seat_id
        ,free
        ,LEAD(free) OVER (ORDER BY seat_id ASC) AS leadcol
        ,LAG(free) OVER (ORDER BY seat_id ASC) AS lagcol
    FROM Cinema
),
cte2 AS (
    SELECT
        *
        ,CASE WHEN free = 1 AND leadcol = 1 AND lagcol IS NULL THEN seat_id 
            WHEN free = 1 AND leadcol = 1 AND lagcol = 0 THEN seat_id
            WHEN free = 1 AND leadcol = 1 AND lagcol = 1 THEN seat_id
            WHEN free = 1 AND leadcol IS NULL AND lagcol = 1 THEN seat_id
            WHEN free =1 AND leadcol = 0 AND lagcol = 1 THEN seat_id
    END AS consec
    FROM cte1
)
SELECT
    consec AS seat_id
FROM cte2
WHERE consec IS NOT NULL
;
```

## Site Solution

```sql
-- LeetCode Solution 
select distinct a.seat_id
from cinema a join cinema b
  on abs(a.seat_id - b.seat_id) = 1
  and a.free = true and b.free = true
order by a.seat_id
;

-- Code Author: Clayton Wong
-- https://leetcode.com/problems/consecutive-available-seats/solutions/597149/mysql-solution
SELECT seat_id
FROM cinema
WHERE free = 1 AND (
    seat_id - 1 IN (SELECT seat_id FROM cinema WHERE free = 1)
    OR
    seat_id + 1 IN (SELECT seat_id FROM cinema WHERE free = 1)
);
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
