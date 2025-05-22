-- Write your PostgreSQL query statement below

-- Triangle judgement
select x
    , y
    , z
    , case 
        when (x + y) > z and (x + z) > y and (y + z) > x then 'Yes'
        else 'No'
    end as triangle
from triangle
;

-- Consecutive numbers
-- Approach 1
select distinct a.num as consecutiveNums
from logs a
left join logs b
on a.id + 1 = b.id
left join logs c
on b.id + 1 = c.id
where a.num = b.num and b.num = c.num
;

-- Approach 2
with cte as (
    select id
        , num
        , lead(num, 1) over(order by id) num_
        , lead(num, 2) over(order by id) num__
    from logs
)
select distinct num as consecutiveNums
from cte
where num = num_ and num_ = num__
;