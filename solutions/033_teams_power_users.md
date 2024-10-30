# SQL Everyday \#033

## Teams Power Users

Site: DataLemur\
Difficulty per Site: Easy

## Problem

Write a query to identify the top 2 Power Users who sent the highest number of messages on Microsoft Teams in August 2022. Display the IDs of these 2 users along with the total number of messages they sent. Output the results in descending order based on the count of the messages. [[Full Description](https://datalemur.com/questions/teams-power-users)]

## Submitted Solution

```sql
-- Submitted Solution
SELECT 
  sender_id
  ,COUNT(sender_id) AS message_count
FROM messages
WHERE sent_date BETWEEN '07/31/2022' AND '09/01/2022'
GROUP BY sender_id
ORDER BY message_count DESC
LIMIT 2;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT 
  sender_id,
  COUNT(message_id) AS count_messages
FROM messages
WHERE EXTRACT(MONTH FROM sent_date) = '8'
  AND EXTRACT(YEAR FROM sent_date) = '2022'
GROUP BY sender_id
ORDER BY count_messages DESC
LIMIT 2; 
```

## Notes

TODO

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
