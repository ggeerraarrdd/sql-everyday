# SQL Everyday \#188

## The Winner University

Site: LeetCode\
Difficulty per Site: Easy

## Problem

There is a competition between New York University and California University. The competition is held between the same number of students from both universities. The university that has more **excellent students** wins the competition. If the two universities have the same number of **excellent students**, the competition ends in a draw.

An **excellent student** is a student that scored `90%` or more in the exam.

Return:

* **"New York University"** if New York University wins the competition.
* **"California University"** if California University wins the competition.
* **"No Winner"** if the competition ends in a draw. [[Full Description](https://leetcode.com/problems/the-winner-university/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
    SELECT
        'New York University' AS university
        ,COUNT(DISTINCT student_id) AS student_count
    FROM NewYork
    WHERE score >= 90
    GROUP BY university
    UNION
    SELECT
        'California University' AS university
        ,COUNT(DISTINCT student_id) AS student_count
    FROM California
    WHERE score >= 90
    GROUP BY university
),
cte2 AS (
    SELECT
        *
        ,1.0 * student_count / SUM(student_count) OVER () AS percentage
    FROM cte1
)
SELECT
    CASE WHEN percentage = 0.5 THEN 'No Winner' ELSE university END AS winner
FROM cte2
ORDER BY student_count DESC
LIMIT 1
;
```

## Site Solution

```sql
-- LeetCode Solution 
SELECT 
  CASE 
    WHEN NY.excellent_students > CA.excellent_students THEN 'New York University'
    WHEN NY.excellent_students < CA.excellent_students THEN 'California University'
    ELSE 'No Winner'
  END AS winner
FROM 
  (
    SELECT 
      COUNT(*) as excellent_students 
    FROM 
      NewYork 
    WHERE 
      score >= 90
  ) NY, 
  (
    SELECT 
      COUNT(*) as excellent_students 
    FROM 
      California 
    WHERE 
      score >= 90
  ) CA;
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
