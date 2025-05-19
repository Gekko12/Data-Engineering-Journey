-- Write your PostgreSQL query statement below

-- Biggest single number
-- Approach 1
with cte as (
    select num
    from mynumbers
    group by num
    having count(num) = 1
)
select max(num) as num
from cte
;

-- Approach 2
select (
    select num 
    from mynumbers 
    group by num 
    having count(num) = 1 
    order by num desc 
    limit 1) as num
    ;