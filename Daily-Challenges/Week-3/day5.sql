-- Write your PostgreSQL query statement below

-- Game Play Analysis IV

-- Approach I
with date_filter as (
    select *
        , lead(event_date) over(partition by player_id order by event_date) as next_event_Date
        , rank() over(partition by player_id order by event_date) as rnk
    from activity
)
select round(sum(case when event_date + 1 = next_event_date then 1 else 0 end) ::numeric / count(player_id), 2) as fraction
from date_filter
where rnk = 1
;

-- Approach II
with cte as(
    select player_id, min(event_date) first_login
    from activity
    group by player_id
)
select round(count(a2.player_id) / (select count(*) from cte)::numeric, 2) as fraction
from activity a1
join cte a2
on a1.player_id = a2.player_id
where a1.event_date = a2.first_login + 1 
;