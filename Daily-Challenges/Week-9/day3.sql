-- Write your PostgreSQL query statement below

-- analyze-subscription-conversion

-- Approach 1
select a.user_id
    , round(avg(case when activity_type = 'free_trial' then activity_duration else null end) :: numeric, 2) as trial_avg_duration
    , round(avg(case when activity_type = 'paid' then activity_duration else null end) :: numeric, 2) as paid_avg_duration
from userActivity a
where exists (
    select b.user_id
    from userActivity b
    where a.user_id = b.user_id
    and b.activity_type not in ('free_trial', 'cancelled')
)
group by user_id
order by user_id
;

-- Approach 2
select * 
from (
    select user_id
        , round(avg(case when activity_type ='free_trial' then activity_duration else null end) :: numeric, 2) as trial_avg_duration
        , round(avg(case when activity_type = 'paid' then activity_duration else null end) :: numeric, 2) as paid_avg_duration
    from UserActivity 
    group by user_id
) T 
where paid_avg_duration is not null
order by user_id