# SQL Everyday \#175

## Form a Chemical Bond

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Two elements can form a bond if one of them is `'Metal'` and the other is `'Nonmetal'`.

Write a solution to find all the pairs of elements that can form a bond.

Return the result table **in any order**. [[Full Description](https://leetcode.com/problems/form-a-chemical-bond/description/)]

## Submitted Solution

```sql
-- Submitted Solution
-- Write your PostgreSQL query statement below
WITH noble AS (
    SELECT
        symbol
    FROM Elements
    WHERE type = 'Metal'
),
nonmetal AS (
    SELECT
        symbol
    FROM Elements
    WHERE type = 'Nonmetal'
)
SELECT
    n.symbol AS metal
    ,nm.symbol AS nonmetal
FROM noble AS n
CROSS JOIN nonmetal AS nm
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- Using JOIN + Filtering
-- Code Author Naveen Kumar Vadlamudi
-- https://leetcode.com/problems/form-a-chemical-bond/solutions/2850891/solution-using-join-filtering

SELECT M.SYMBOL AS METAL, NM.SYMBOL AS NONMETAL
FROM 
( SELECT SYMBOL FROM ELEMENTS AS E WHERE E.TYPE = 'Metal' ) AS M ,
( SELECT SYMBOL FROM ELEMENTS AS E  WHERE E.TYPE = 'Nonmetal' ) AS NM 

-- Code Author Lalit Das
-- https://leetcode.com/problems/form-a-chemical-bond/solutions/2845961/cross-join-with-condition
select 
a.symbol as metal,
b.symbol as nonmetal
from 
Elements as a,
Elements as b
where a.type= "Metal" and b.type="Nonmetal"
```

## Notes

TBD

## NB

`CROSS JOIN`

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
