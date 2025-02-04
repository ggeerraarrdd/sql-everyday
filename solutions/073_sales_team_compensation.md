# SQL Everyday \#073

## Sales Team Compensation

Site: DataLemur\
Difficulty per Site: Medium

## Problem

As the Sales Operations Analyst at Oracle, you have been tasked with assisting the VP of Sales in determining the final compensation earned by each salesperson for the year. The compensation structure includes a fixed base salary, a commission based on total deals, and potential accelerators for exceeding their quota.

Each salesperson earns a fixed base salary and a percentage of commission on their total deals. Also, if they beat their quota, any sales after that receive an accelerator, which is just a higher commission rate applied to their commissions after they hit the quota.

Write a query that calculates the total compensation earned by each salesperson. The output should include the employee ID and their corresponding total compensation, sorted in descending order. In the case of ties, the employee IDs should be sorted in ascending order.

Assumptions:

* A salesperson is considered to have hit their target (quota) if their total deals meet or exceed the assigned quota.
* If a salesperson does not meet the target, their compensation package consists of the fixed base salary and a commission based on the total deals.
* If a salesperson meets the target, their compensation package includes
  * The fixed base salary,
  * A commission on target (quota), and
  * An additional commission, including any accelerator on the remaining balance of the total deals (total deals - quota). The accelerator represents a higher commission rate for sales made beyond the quota. [[Full Description](https://datalemur.com/questions/sales-team-compensation)]

## Submitted Solution

```sql
-- Submitted Solution
/**
Total Compensation = Base Salary + Commission on Target + Commission on Excess Sales
Total Compensation = $60,000 + (10% * $500,000) + (10% * (Total Deals - Quota) * Accelerator)
Total Compensation = $60,000 +$50,000 + $45,000 = $155,000
**/

WITH cte AS (
SELECT
  employee_id
  ,SUM(deal_size) AS total_deals
FROM deals
GROUP BY employee_id
)
SELECT
  c.employee_id
  ,e.base -- Base Salary
    + (e.commission * CASE WHEN c.total_deals > e.quota THEN e.quota ELSE c.total_deals END) -- Commission on Target
    + (e.commission * (CASE WHEN c.total_deals - e.quota > 0 THEN c.total_deals - e.quota ELSE 0 END) * e.accelerator) -- Commission on Excess Sales
    AS total_compensation
FROM cte AS c
JOIN employee_contract AS e ON c.employee_id = e.employee_id
ORDER BY total_compensation DESC, c.employee_id ASC
;
```

## Site Solution

```sql
-- DataLemur Solution 
SELECT 
  deals.employee_id,
  CASE 
    WHEN SUM(deals.deal_size) <= employee.quota 
      THEN employee.base + (employee.commission * SUM(deals.deal_size)) -- #1
    ELSE employee.base + (employee.commission * employee.quota) + 
      ((SUM(deals.deal_size) - employee.quota) * employee.commission * employee.accelerator) -- #2
  END AS total_compensation
FROM deals
INNER JOIN employee_contract AS employee
  ON deals.employee_id = employee.employee_id
GROUP BY deals.employee_id, employee.quota, employee.base, employee.commission, employee.accelerator
ORDER BY total_compensation DESC, deals.employee_id;
```

## Notes

TODO

## NB

TBD

Go to [Index](../?tab=readme-ov-file#index)\
Go to [Overview](../?tab=readme-ov-file)
