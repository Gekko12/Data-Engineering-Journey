-- Write your PostgreSQL query statement below

-- find-overbooked-employees
with cte_meet_hours as (
    select employee_id
        , date_part('week', meeting_date) as week_number
        , sum(duration_hours) as sum_duration_hours
    from meetings
    group by 1, 2
)
select emp.employee_id
    , emp.employee_name
    , emp.department
    , count(emp.employee_id) as meeting_heavy_weeks
from cte_meet_hours as cmh
join employees as emp
on cmh.employee_id = emp.employee_id
where sum_duration_hours > 20
group by 1, 2, 3
having count(emp.employee_id) > 1
order by 4 desc, 2
;
