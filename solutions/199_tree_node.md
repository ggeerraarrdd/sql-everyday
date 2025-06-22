# SQL Everyday \#199

## Tree Node

Site: LeetCode\
Difficulty per Site: Medium

## Problem

Write a solution to report the type of each node in the tree.

Return the result table in **any order**. [[Full Description](https://leetcode.com/problems/tree-node/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
    SELECT
        t1.id AS node
        ,COUNT(DISTINCT t1.p_id) AS parent_nodes
        ,COUNT(DISTINCT t2.p_id) AS child_nodes
    FROM Tree AS t1
    LEFT JOIN Tree as t2 ON t1.id = t2.p_id  
    GROUP BY node
)
SELECT
    node AS id
    ,CASE WHEN parent_nodes = 0 THEN 'Root'
        WHEN parent_nodes > 0 AND child_nodes = 0 THEN 'Leaf'
        ELSE 'Inner' END AS type
FROM cte 
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- Approach 1: Using `UNION`
SELECT
    id, 'Root' AS Type
FROM
    tree
WHERE
    p_id IS NULL

UNION

SELECT
    id, 'Leaf' AS Type
FROM
    tree
WHERE
    id NOT IN (SELECT DISTINCT
            p_id
        FROM
            tree
        WHERE
            p_id IS NOT NULL)
        AND p_id IS NOT NULL

UNION

SELECT
    id, 'Inner' AS Type
FROM
    tree
WHERE
    id IN (SELECT DISTINCT
            p_id
        FROM
            tree
        WHERE
            p_id IS NOT NULL)
        AND p_id IS NOT NULL
ORDER BY id;

-- Approach 2: Using flow control statement CASE
SELECT
    id AS `Id`,
    CASE
        WHEN tree.id = (SELECT atree.id FROM tree atree WHERE atree.p_id IS NULL)
          THEN 'Root'
        WHEN tree.id IN (SELECT atree.p_id FROM tree atree)
          THEN 'Inner'
        ELSE 'Leaf'
    END AS Type
FROM
    tree
ORDER BY `Id`
;
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
