-- Write your PostgreSQL query statement below

-- Friend requests ii who has the most friends
-- Approach 1
with cte1 as (
    select requester_id
        , count(*) as r_cnt
    from requestAccepted
    group by requester_id
)
, cte2 as (
    select accepter_id 
        , count(*) as a_cnt
    from requestAccepted
    group by accepter_id 
)
select coalesce(requester_id, accepter_id) as id
    , coalesce(r_cnt, 0) + coalesce(a_cnt, 0) as num
from cte1
full outer join cte2
on cte1.requester_id = cte2.accepter_id
order by num desc
limit 1 
;

-- Approach 2
with cte as (
    select requester_id as id
    from requestAccepted 
    union all
    select accepter_id
    from requestAccepted 
)
select id, count(1) num
from cte
group by id
order by num desc
limit 1
;

-- Investements in 2016
-- Approach -1
select round(sum(t1.tiv_2016)::numeric, 2) tiv_2016
from insurance t1
where t1.tiv_2015 in (
    select t2.tiv_2015
    from insurance t2
    group by t2.tiv_2015
    having count(*) > 1
    )
and (lat, lon) in (
    select lat, lon
    from insurance
    group by lat, lon
    having count(*) = 1 
    )
;

-- Approach -2
with cte AS(
    select pid,
        tiv_2015,
        tiv_2016 ,
        count(pid)OVER(partition by tiv_2015 ) AS tv_cnt,
        count(pid)OVER(partition by lat,lon) AS l_cnt 
from insurance
)
select round(sum(tiv_2016)::numeric,2) AS tiv_2016  
from cte
where tv_cnt > 1 
and l_cnt < 2
;