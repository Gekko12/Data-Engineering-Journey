-- Write your PostgreSQL query statement below

-- Employees whose manager left the company

-- Approach 1
select e1.employee_id
from employees e1
where e1.salary < 30000 and e1.manager_id not in (
    select e2.employee_id
    from employees e2
)
order by employee_id
;

-- Appraoch 2
select e1.employee_id
from employees e1
left join employees e2
on e1.manager_id = e2.employee_id
where e1.manager_id is not null
and e1.salary < 30000
and e2.employee_id is null 
order by e1.employee_id
;