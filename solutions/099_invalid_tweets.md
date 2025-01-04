# SQL Everyday \#099

## Invalid Tweets

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is *strictly greater* than `15`.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/invalid-tweets/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    tweet_id
FROM Tweets
WHERE LENGTH(content) > 15
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- Site solution essentially the same.
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
