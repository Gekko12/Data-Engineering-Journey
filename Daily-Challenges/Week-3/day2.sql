-- Write your PostgreSQL query statement below

-- Project employees I
select pro.project_id
    , round(avg(emp.experience_years)::numeric, 2) average_years
from project pro
join employee emp
on pro.employee_id = emp.employee_id
group by pro.project_id
;

-- Percentage of users attended a contest
with cte as (
    select count(*) user_count
    from users usr
)
select rgr.contest_id
    , round((count(rgr.user_id) * 100.0) / cte.user_count, 2) percentage
from users usr
join register rgr
on usr.user_id = rgr.user_id
cross join cte
group by rgr.contest_id, cte.user_count
order by percentage desc, rgr.contest_id asc
;
