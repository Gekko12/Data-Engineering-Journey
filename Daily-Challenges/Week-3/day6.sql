-- Write your PostgreSQL query statement below

-- Number of unique subjects taught by each teacher
select teacher_id, count(distinct subject_id) as cnt
from teacher
group by teacher_id
;

-- User activity for the past 30 days I
select activity_date as day
    , count(distinct user_id) as active_users
from activity
where activity_date <= '2019-07-27' :: date and activity_date > ('2019-07-27' :: date - 30)
group by activity_date