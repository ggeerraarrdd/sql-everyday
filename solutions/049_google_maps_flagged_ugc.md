# SQL Everyday \#049

## Google Maps Flagged UGC

Site: DataLemur\
Difficulty per Site: Medium

## Problem

As a Data Analyst on the Google Maps User Generated Content team, you and your Product Manager are investigating user-generated content (UGC) – photos and reviews that independent users upload to Google Maps.

Write a query to determine which type of place (`place_category`) attracts the most UGC tagged as "off-topic". In the case of a tie, show the output in ascending order of `place_category`. [[Full Description](https://datalemur.com/questions/off-topic-maps-ugc)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte AS (
  SELECT
    place_category
    ,COUNT(*)
  FROM place_info AS p
  LEFT JOIN maps_ugc_review AS m ON p.place_id = m.place_id
  WHERE content_tag = 'Off-topic'
  GROUP BY place_category
  ORDER BY count DESC, place_category ASC
)
SELECT
  place_category AS off_topic_places
FROM cte
WHERE count = (SELECT MAX(count) FROM cte)
;
```

## Site Solution

```sql
-- DataLemur Solution 
WITH reviews AS (
  SELECT
    place_category,
    COUNT(ugc.content_id) AS content_count
  FROM place_info place
  INNER JOIN maps_ugc_review ugc
    ON place.place_id = ugc.place_id
  WHERE LOWER(content_tag) = 'off-topic'
  GROUP BY place_category
)
, top_place_category AS (
  SELECT
    place_category,
    content_count,
    RANK() OVER (
      ORDER BY content_count DESC) AS top_place
  FROM reviews
)

SELECT place_category AS off_topic_places
FROM top_place_category
WHERE top_place = 1;
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
