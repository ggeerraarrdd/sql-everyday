# SQL Everyday \#032

## Marketing Touch Streak

Site: DataLemur\
Difficulty per Site: Hard

## Problem

As a Data Analyst on Snowflake's Marketing Analytics team, your objective is to analyze customer relationship management (CRM) data and identify contacts that satisfy two conditions:

1. Contacts who had a marketing touch for three or more consecutive weeks.
2. Contacts who had at least one marketing touch of the type 'trial_request'.

Marketing touches, also known as touch points, represent the interactions or points of contact between a brand and its customers.

Your goal is to generate a list of email addresses for these contacts. [[Full Description](https://datalemur.com/questions/marketing-touch-streak)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
  SELECT
    *
    ,EXTRACT(WEEK FROM event_date) AS week
    ,LAG(EXTRACT(WEEK FROM event_date), 1) OVER (PARTITION BY contact_id ORDER BY event_date DESC) AS week_lag
  FROM marketing_touches
  WHERE contact_id IN (SELECT contact_id FROM marketing_touches WHERE event_type = 'trial_request')
  ORDER BY contact_id ASC
),
cte2 AS (
  SELECT
    *
    ,week - COALESCE(week_lag, week) AS diff
    ,ROW_NUMBER() OVER (PARTITION BY contact_id ORDER BY event_date DESC) AS rownum
  FROM cte1
)
SELECT
  email
FROM cte2
JOIN crm_contacts AS crm ON cte2.contact_id = crm.contact_id
WHERE diff = -1 AND rownum = 3
;
```

## Site Solution

```sql
-- DataLemur Solution 
WITH consecutive_events_cte AS (
  SELECT
    event_id,
    contact_id, 
    event_type, 
    DATE_TRUNC('week', event_date) AS current_week,
    LAG(DATE_TRUNC('week', event_date)) OVER (
      PARTITION BY contact_id 
      ORDER BY DATE_TRUNC('week', event_date)) AS lag_week,
    LEAD(DATE_TRUNC('week', event_date)) OVER (
      PARTITION BY contact_id 
      ORDER BY DATE_TRUNC('week', event_date)) AS lead_week
FROM marketing_touches)

SELECT DISTINCT contacts.email
FROM consecutive_events_cte AS events
INNER JOIN crm_contacts AS contacts
  ON events.contact_id = contacts.contact_id
WHERE events.lag_week = events.current_week - INTERVAL '1 week'
  OR events.lead_week = events.current_week + INTERVAL '1 week'
  AND events.contact_id IN (
    SELECT contact_id 
    FROM marketing_touches 
    WHERE event_type = 'trial_request'
  );
```

## Notes

TODO

## NB

TBD

Go to [Table of Contents](/README.md#contents)\
Go to [Overview](/README.md)
