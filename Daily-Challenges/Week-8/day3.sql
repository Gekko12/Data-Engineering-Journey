-- Write your PostgreSQL query statement below

-- employees-with-missing-information

-- Approach 1
select coalesce(emp.employee_id, slr.employee_id) as employee_id
from employees emp
full outer join salaries slr
on emp.employee_id = slr.employee_id
where emp.employee_id is null
or slr.employee_id is null
order by employee_id
;

-- Approach 2
select employee_id
from employees
where employee_id not in (select employee_id from salaries)
union
select employee_id
from salaries
where employee_id not in (select employee_id from employees)
order by employee_id
;