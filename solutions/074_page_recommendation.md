# SQL Everyday \#074

## Page Recommendation

Site: DataLemur\
Difficulty per Site: Hard

## Problem

Write a query to recommend a page to a user. A recommendation is based on a page liked by user friends. Assume you have two tables: a two-column table of users and their friends, and a two-column table of users and the pages they liked.

Assumptions:

* Only recommend the top page to the user, and do not recommend pages that were already liked by the user.
* Top page is defined as the page with the highest number of followers.

Output the user id and page recommended. Order the result in ascending order by user id. [[Full Description](https://datalemur.com/questions/page-recommendation)]

## Submitted Solution

```sql
-- Submitted Solution
WITH cte1 AS (
  SELECT
    DISTINCT user_id AS user_id
  FROM friendship
  UNION
  SELECT
    DISTINCT friend_id AS user_id
  FROM friendship
),
cte2 AS (
  SELECT
    c.user_id
    ,COALESCE(f1.friend_id, f2.user_id, f2.friend_id) AS friend_id
  FROM cte1 AS c
  LEFT JOIN friendship AS f1 ON c.user_id = f1.user_id
  LEFT JOIN friendship AS f2 ON c.user_id = f2.friend_id
),
cte3 AS (
  SELECT
    c.user_id
    ,p.page_id
    ,COUNT(p.page_id) AS cnt
  FROM cte2 AS c 
  JOIN page_following AS p ON c.friend_id = p.user_id
  GROUP BY c.user_id, p.page_id
),
cte4 AS (
  SELECT
    c.*
    ,RANK() OVER (PARTITION BY c.user_id ORDER BY cnt DESC) AS rnk
  FROM cte3 AS c 
  LEFT JOIN page_following AS p2 ON c.user_id = p2.user_id 
      AND c.page_id = p2.page_id
  WHERE p2.page_id IS NULL
  ORDER BY c.user_id, c.cnt DESC
)
SELECT
  user_id
  ,page_id AS Page_Recommended
FROM cte4
WHERE rnk = 1
;
```

## Site Solution

```sql
-- DataLemur Solution 
WITH two_way_friendship AS (
  SELECT user_id, friend_id
  FROM friendship
  UNION
  SELECT friend_id, user_id
  FROM friendship
  
), recommended_pages AS (
  SELECT
    friends.user_id,
    pages.page_id,
    COUNT(*) AS followers
  FROM two_way_friendship AS friends
  LEFT JOIN page_following AS pages
    ON friends.friend_id = pages.user_id
  WHERE NOT EXISTS (
    SELECT id
    FROM page_following AS pages_2
    WHERE friends.user_id = pages_2.user_id
      AND pages.page_id = pages_2.page_id)
  GROUP BY friends.user_id, pages.page_id
  
), top_pages AS (
  SELECT
    user_id,
    page_id,
    followers,
    DENSE_RANK() OVER (
      PARTITION BY user_id ORDER BY followers DESC) AS rnk
  FROM recommended_pages)

SELECT user_id, page_id
FROM top_pages
WHERE rnk = 1
ORDER BY user_id;
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
