-- Write your PostgreSQL query statement below

-- Count salary categories 
select 'Low Salary' as category 
    , sum(case when income < 20000 then 1 else 0 end) accounts_count
from accounts
union
select 'Average Salary' 
    , sum(case when income between 20000 and 50000 then 1 else 0 end) 
from accounts
union
select 'High Salary' 
    , sum(case when income > 50000 then 1 else 0 end)
from accounts
;