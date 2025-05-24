-- Write your PostgreSQL query statement below

-- Last person to fit in the bus
with cte as (
    select turn
        , person_id 
        , person_name
        , weight 
        , sum(weight) over(order by turn) as cumulative_weight
    from queue
)
select person_name
from cte
where cumulative_weight <= 1000
order by turn desc
limit 1
;