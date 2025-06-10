-- Write your PostgreSQL query statement below

-- capital-gainloss
-- Approach 1 
select stock_name
    , sum(case when operation = 'Sell' then price else 0 end) 
        - sum(case when operation = 'Buy' then price else 0 end) 
    as capital_gain_loss
from stocks
group by stock_name
;

-- Approach 2
select stock_name
    , sum(case when operation = 'Sell' then price else -price end) as capital_gain_loss
from stocks
group by stock_name
;

