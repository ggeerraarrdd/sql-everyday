# SQL Everyday \#001

## Histogram of Tweets

Site: DataLemur\
Difficulty per Site: Easy

## Problem

Assume you're given a table Twitter tweet data, write a query to obtain a histogram of tweets posted per user in 2022. Output the tweet count per user as the bucket and the number of Twitter users who fall into that bucket. In other words, group the users by the number of tweets they posted in 2022 and count the number of users in each group. [[Full Description](https://datalemur.com/questions/sql-histogram-tweets)]

## Submitted Solution

```sql
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
  ,COUNT(useR_id) AS users_num
FROM cte 
GROUP BY count
;
```

## Site Solution

```sql
-- TBD
```

## Notes

TODO

## NB

TBD

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
