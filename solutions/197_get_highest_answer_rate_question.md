# SQL Everyday \#197

## Get Highest Answer Rate Question

Site: LeetCode\
Difficulty per Site: Medium

## Problem

The **answer rate** for a question is the number of times a user answered the question by the number of times a user showed the question.

Write a solution to report the question that has the highest **answer rate**. If multiple questions have the same maximum **answer rate**, report the question with the smallest `question_id`. [[Full Description](https://leetcode.com/problems/get-highest-answer-rate-question/)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
    SELECT
        question_id
        ,1.00 * SUM(CASE WHEN action = 'answer' THEN 1 ELSE 0 END) /
        SUM(CASE WHEN action = 'show' THEN 1 ELSE 0 END) AS rate
    FROM SurveyLog
    GROUP BY question_id
),
cte2 AS (
    SELECT
        question_id
        ,ROW_NUMBER() OVER (ORDER BY rate DESC, question_id ASC) AS rownum
    FROM cte1
)
SELECT
    question_id AS survey_log
FROM cte2
WHERE rownum = 1
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- Approach 1: Getting the Highest and the Smallest Using RANK()
WITH answer_rate AS
   (
   SELECT question_id, 
   SUM(CASE WHEN action = 'answer' THEN 1 ELSE 0 END) 
   / SUM(CASE WHEN action = 'show' THEN 1 ELSE 0 END) AS rate
   FROM surveylog
   GROUP BY question_id
   )
SELECT question_id AS survey_log
FROM 
   (
   SELECT question_id, 
      RANK()OVER(ORDER BY rate DESC question_id) AS rnk
   FROM answer_rate
   ) AS t0
WHERE rnk = 1

-- Approach 2: Getting the Highest and the Smallest Using ORDER BY + LIMIT
SELECT question_id AS survey_log
 FROM surveylog
 GROUP BY question_id
 ORDER BY SUM(CASE WHEN action = 'answer' THEN 1 ELSE 0 END)
   / SUM(CASE WHEN action = 'show' THEN 1 ELSE 0 END) DESC
   , question_id ASC
 LIMIT 1
```

## Notes

TBD

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
