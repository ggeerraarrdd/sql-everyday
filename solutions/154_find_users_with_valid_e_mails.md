# SQL Everyday \#154

## Find Users With Valid E-Mails

Site: LeetCode\
Difficulty per Site: Easy

## Problem

Write a solution to find the users who have *valid emails*.

A valid e-mail has a prefix name and a domain where:

* *The prefix name* is a string that may contain letters (upper or lower case), digits, underscore `'_'`, period `'.'`, and/or dash `'-'`. The prefix name *must* start with a letter.
* The domain is `'@leetcode.com'`.

Return the result table in *any order*. [[Full Description](https://leetcode.com/problems/find-users-with-valid-e-mails/description/)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT
    user_id
    ,name
    ,mail
FROM Users
WHERE mail ~ '^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\.com$'
;
```

## Site Solution

```sql
-- LeetCode Solution 
-- TBD
```

## Notes

TBD

## NB

Regex

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
