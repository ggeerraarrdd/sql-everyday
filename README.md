# SQL Everyday

One SQL problem a day for a year

## Description

_SQL Everyday_ is a personal challenge to solve at least one SQL problem everyday for the next 365 days, starting from September 28, 2024.

The problems are selected from various websites devoted to online learning and technical job interview preparations. Below is a current list of these websites.

* [Codewars](https://www.codewars.com/)
* [DataCamp](https://www.datacamp.com/)
* [DataLemur](https://datalemur.com/)
* [LeetCode](https://leetcode.com/)

Besides having the required set of SQL problems, they were chosen because they have an integrated database environment to work through to a solution.

All submitted solutions are then stored in this repo in their own markdown file. See the [Contents](#contents) section below for an index of those solutions.

To make the daily tasks of creating a new file and updating the index easier, there is a [Jupyter notebook to automate that process](templates/solution.ipynb).

![Coeus](resources/coeus.jpg)
(_Coeus, whose name is derived from the Greek word 'koios', meaning 'query' or 'questioning', and who is associated with knowledge, determination and the inquisitive mind, here depicted second Titan from the left by Gustave Doré while attempting to solve a difficult SQL problem._)

## Disclaimer

ALL CONTENTS IN THIS REPO ARE FOR EDUCATIONAL PURPOSES ONLY.

## Getting Started

### Dependencies

* See `requirements.txt`

### Usage

* To automatically create a new solution file, open [`solution.ipynb`](templates/solution.ipynb) in the `templates` directory and follow instructions.
* To check out submitted solutions and how they compare to those provided by the site, see `Contents` below.

## Contents

| Day   | Title                                                                                               | Solution  | Site        | Difficulty  | N2SELF               |
| ----- | --------------------------------------------------------------------------------------------------- | --------- | ----------- | ----------- | -------------------- |
| 001   | [Histogram of Tweets](https://datalemur.com/questions/sql-histogram-tweets)                         | [Solution](solutions/001_histogram_of_tweets.md) | DataLemur | Easy |  |
| 002   | [User's Third Transaction](https://datalemur.com/questions/sql-third-transaction)                   | [Solution](solutions/002_users_third_transaction.md) | DataLemur | Medium |  |
| 003   | [Second Highest Salary](https://datalemur.com/questions/sql-second-highest-salary)                  | [Solution](solutions/003_second_highest_salary.md) | DataLemur | Medium |  |
| 004   | [Sending vs. Opening Snaps](https://datalemur.com/questions/time-spent-snaps)                       | [Solution](solutions/004_sending_vs_opening_snaps.md) | DataLemur | Medium | `FILTER()`  |
| 005   | [Highest-Grossing Items](https://datalemur.com/questions/sql-highest-grossing)                      | [Solution](solutions/005_highest-grossing_items.md) | DataLemur | Medium | `RANK()` vs `DENSE_RANK`  |
| 006   | [Top Three Salaries](https://datalemur.com/questions/sql-top-three-salaries)                        | [Solution](solutions/006_top_three_salaries.md) | DataLemur  | Medium |   |
| 007   | [Top 5 Artists](https://datalemur.com/questions/top-fans-rank)                                      | [Solution](solutions/007_top_5_artists.md) | DataLemur  | Medium |   |
| 008   | [Signup Activation Rate](https://datalemur.com/questions/signup-confirmation-rate)                  | [Solution](solutions/008_signup_activation_rate.md) | DataLemur | Medium |   |
| 009   | [Supercloud Customer](https://datalemur.com/questions/supercloud-customer)                          | [Solution](solutions/009_supercloud_customer.md) | DataLemur | Medium |   |
| 010   | [Odd and Even Measurements](https://datalemur.com/questions/odd-even-measurements)                  | [Solution](solutions/010_odd_and_even_measurements.md) | DataLemur | Medium | `MOD()`  |
| 011   | [Histogram of Users and Purchases](https://datalemur.com/questions/histogram-users-purchases)       | [Solution](solutions/011_histogram_of_users_and_purchases.md) | DataLemur | Medium |   |
| 012   | [Compressed Mode](https://datalemur.com/questions/alibaba-compressed-mode)                          | [Solution](solutions/012_compressed_mode.md) | DataLemur | Medium | `MODE()`  |
| 013   | [Card Launch Success](https://datalemur.com/questions/card-launch-success)                          | [Solution](solutions/013_card_launch_success.md) | DataLemur | Medium |   |
| 014   | [International Call Percentage](https://datalemur.com/questions/international-call-percentage)      | [Solution](solutions/014_international_call_percentage.md) | DataLemur | Medium |   |
| 015   | [Histogram of Tweets](https://datalemur.com/questions/sql-histogram-tweets)                         | [Solution](solutions/015_histogram_of_tweets.md) | DataLemur | Easy | `EXTRACT()` vs `BETWEEN`  |
| 016   | [Patient Support Analysis (Part 2)](https://datalemur.com/questions/uncategorized-calls-percentage) | [Solution](solutions/016_patient_support_analysis_part_2.md) | DataLemur | Medium |   |
| 017   | [Active User Retention](https://datalemur.com/questions/user-retention)                             | [Solution](solutions/017_active_user_retention.md) | DataLemur | Hard |   |
| 018   | [Data Science Skills](https://datalemur.com/questions/matching-skills)                              | [Solution](solutions/018_data_science_skills.md) | DataLemur | Easy |   |
| 019   | [FAANG Stock Min-Max (Part 1)](https://datalemur.com/questions/sql-bloomberg-stock-min-max-1)       | [Solution](solutions/019_faang_stack_min-max_part_1.md) | DataLemur | Medium |   |
| 020   | [Y-on-Y Growth Rate](https://datalemur.com/questions/yoy-growth-rate)                               | [Solution](solutions/020_y-on-y_growth_rate.md) | DataLemur | Hard | `LAG()`  |
| 021   | [Page With No Likes](https://datalemur.com/questions/sql-page-with-no-likes)                        | [Solution](solutions/021_page_with_no_likes.md) | DataLemur | Easy |   |
| 022   | [Swapped Food Delivery](https://datalemur.com/questions/sql-swapped-food-delivery)                  | [Solution](solutions/022_swapped_food_delivery.md) | DataLemur | Medium |   |
| 023   | [Median Google Search Frequency](https://datalemur.com/questions/median-search-freq)                | [Solution](solutions/023_median_google_search_frequency.md) | DataLemur | Hard | `GENERATE_SERIES()`, `PERCENTILE_CONT()`  |
| 024   | [Unfinished Parts](https://datalemur.com/questions/tesla-unfinished-parts)                          | [Solution](solutions/024_unfinished_parts.md) | DataLemur | Easy |   |
| 025   | [Fill Missing Client Data](https://datalemur.com/questions/fill-missing-product)                    | [Solution](solutions/025_fill_missing_client_data.md) | DataLemur | Medium | `FIRST_VALUE()`  |
| 026   | [Advertiser Status](https://datalemur.com/questions/updated-status)                                 | [Solution](solutions/026_advertiser_status.md) | DataLemur | Hard |   |
| 027   | [Laptop vs. Mobile Viewership](https://datalemur.com/questions/laptop-mobile-viewership)            | [Solution](solutions/027_laptop_vs_mobile_viewership.md) | DataLemur | Easy |   |
| 028   | [Spotify Streaming History](https://datalemur.com/questions/spotify-streaming-history)              | [Solution](solutions/028_spotify_streaming_history.md) | DataLemur | Medium |   |
| 029   | [Consecutive Filing Years](https://datalemur.com/questions/consecutive-filing-years)                | [Solution](solutions/029_consecutive_filing_years.md) | DataLemur | Hard |   |
| 030   | [Average Post Hiatus (Part 1)](https://datalemur.com/questions/sql-average-post-hiatus-1)           | [Solution](solutions/030_average_post_hiatus_part_1.md) | DataLemur | Easy |   |
| 031   | [Mean, Median, Mode](https://datalemur.com/questions/mean-median-mode)                              | [Solution](solutions/031_mean_median_mode.md) | DataLemur | Medium | `PERCENTILE_CONT()`  |
| 032   | [Marketing Touch Streak](https://datalemur.com/questions/marketing-touch-streak)                    | [Solution](solutions/032_marketing_touch_streak.md) | DataLemur | Hard |   |
| 033   | [Teams Power Users](https://datalemur.com/questions/teams-power-users)                              | [Solution](solutions/033_teams_power_users.md) | DataLemur | Easy |   |
| 034   | [Pharmacy Analytics (Part 4)](https://datalemur.com/questions/top-drugs-sold)                       | [Solution](solutions/034_pharmacy_analytics_part_4.md) | DataLemur | Medium |   |
| 035   | [3-Topping Pizzas](https://datalemur.com/questions/pizzas-topping-cost)                             | [Solution](solutions/035_3topping_pizzas.md) | DataLemur | Hard |   |
| 036   | [Well Paid Employees](https://datalemur.com/questions/sql-well-paid-employees)                      | [Solution](solutions/034_well_paid_employees.md) | DataLemur | Easy  |   |
| 037   | [Frequently Purchased Pairs](https://datalemur.com/questions/frequently-purchased-pairs)            | [Solution](solutions/037_frequently_purchased_pairs.md) | DataLemur | Medium | `ARRAY_AGG()`, `ARRAY_LENGTH()`  |
| 038   | [Department vs. Company Salary](https://datalemur.com/questions/sql-department-company-salary-comparison)  | [Solution](solutions/038_department_vs_company_salary.md) | DataLemur | Hard |   |
| 039   | [Final Account Balance](https://datalemur.com/questions/final-account-balance)                      | [Solution](solutions/039_final_account_balance.md) | DataLemur | Easy |   |

## Authors

* [@ggeerraarrdd](https://github.com/ggeerraarrdd/)

## Version History

### Release Notes

* See [https://github.com/ggeerraarrdd/sql-everyday/releases](https://github.com/ggeerraarrdd/sql-everyday/releases)

### Future Work

TBD

## License

* [MIT License](https://github.com/ggeerraarrdd/sql-everyday/blob/main/LICENSE)

## Acknowledgments

* TODO

## Fronticepiece

Plate LXI: 'This proud one / Would of his strength against almighty Jove / Make trial' (Cary). Canto xxxi: Line 82: Page 165. Image taken from Dante Alighieri, Dante's Inferno. Translated by Henry Francis Cary. Illustrated by Gustave Doré. New York, London, and Paris: Cassell & Company Limited, 1866.
