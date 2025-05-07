-- Write your PostgreSQL query statement below

-- Rising temperature
-- Approach 1: Using LAG()
with cte as (
    select *,
        lag(id) over(order by recordDate) as prev_id,
        lag(recordDate) over(order by recordDate) as prev_recordDate,
        lag(temperature) over(order by recordDate) as prev_temperature
    from weather
)
select id
from cte
where temperature > prev_temperature
and recordDate = prev_recordDate + 1;

-- Approach 2: Using Self Inner Join
select w1.id
from weather w1
join weather w2
on w1.recordDate = w2.recordDate + 1
and w1.temperature > w2.temperature;

-- Approach 3: Using Cross Join
select w1.id
from weather w1, weather w2
where w1.recordDate = w2.recordDate + 1
and w1.temperature > w2.temperature;
