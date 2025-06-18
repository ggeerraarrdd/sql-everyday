# SQL Everyday \#198

## Count Student Number in Departments

Site: LeetCode\
Difficulty per Site: Medium

## Problem

Write a solution to report the respective department name and number of students majoring in each department for all departments in the `Department` table (even ones with no current students).

Return the result table ordered by `student_number` **in descending order**. In case of a tie, order them by `dept_name` **alphabetically**. [[Full Description](https://leetcode.com/problems/count-student-number-in-departments/description/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
    SELECT
        d.dept_name
        ,COUNT(DISTINCT student_id) AS student_number
    FROM Student AS s
    JOIN Department AS d ON s.dept_id = d.dept_id
    GROUP BY d.dept_name
)
SELECT
    d.dept_name
    ,COALESCE(student_number, 0) AS student_number
FROM Department AS d
LEFT JOIN cte AS c ON d.dept_name = c.dept_name
ORDER BY student_number DESC, d.dept_name ASC
;
```

## Site Solution

```sql
-- LeetCode Solution 
SELECT
    dept_name, COUNT(student_id) AS student_number
FROM
    department
        LEFT OUTER JOIN
    student ON department.dept_id = student.dept_id
GROUP BY department.dept_name
ORDER BY student_number DESC , department.dept_name
;
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
