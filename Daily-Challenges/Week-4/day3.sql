-- Write your PostgreSQL query statement below

-- Primary department for each employee

-- Approach-1
select employee_id
    , department_id
from employee
where primary_flag = 'Y'
or employee_id in (
    select employee_id
    from employee
    group by employee_id
    having count(department_id) = 1
);

-- Approach-2
with cte as (
    select employee_id
        , count(department_id) as count_department_id
    from employee
    group by employee_id
)
select e1.employee_id, e1.department_id
from employee e1
join cte e2
on e1.employee_id = e2.employee_id
where count_department_id = 1 or primary_flag = 'Y'
;
