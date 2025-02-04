# SQL Everyday \#015

## Histogram of Tweets

Site: DataLemur\
Difficulty per Site: Easy

## Problem

Assume you're given a table Twitter tweet data, write a query to obtain a histogram of tweets posted per user in 2022. Output the tweet count per user as the bucket and the number of Twitter users who fall into that bucket. In other words, group the users by the number of tweets they posted in 2022 and count the number of users in each group. [[Full Description](https://datalemur.com/questions/sql-histogram-tweets)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT
    user_id
    ,COUNT(tweet_id) AS count
  FROM tweets
  WHERE EXTRACT(YEAR FROM tweet_date) = 2022
  GROUP BY user_id
)
SELECT
  count AS tweet_buket
  ,COUNT(user_id) AS users_num
FROM cte 
GROUP BY count
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT 
  tweet_count_per_user AS tweet_bucket, 
  COUNT(user_id) AS users_num 
FROM (
  SELECT 
    user_id, 
    COUNT(tweet_id) AS tweet_count_per_user 
  FROM tweets 
  WHERE tweet_date BETWEEN '2022-01-01' AND '2022-12-31'
  GROUP BY user_id) AS total_tweets 
GROUP BY tweet_count_per_user;
```

## Notes

* Differences between solutions:
  * CTE vs nested query in the `FROM` clause
  * `EXTRACT()` vs `BETWEEN` in the `WHERE` clause to filter dates.

## NB

TBD

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
