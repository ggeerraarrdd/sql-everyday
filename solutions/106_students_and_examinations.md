# SQL Everyday \#106

## Students and Examinations

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to find the number of times each student attended each exam.

Return the result table ordered by `student_id` and `subject_name`. [[Full Description](https://leetcode.com/problems/students-and-examinations/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    st.student_id
    ,st.student_name
    ,su.subject_name
    ,SUM(CASE WHEN ex.student_id IS NULL THEN 0 ELSE 1 END) AS attended_exams
FROM Students AS st
CROSS JOIN subjects AS su
LEFT JOIN Examinations AS ex ON st.student_id = ex.student_id
    AND su.subject_name = ex.subject_name
GROUP BY st.student_id, st.student_name, su.subject_name
ORDER BY st.student_id, su.subject_name
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- TO ADD
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
