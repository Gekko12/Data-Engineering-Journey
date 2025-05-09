-- Write your PostgreSQL query statement below

-- Employee Bonus
select emp.name, bon.bonus
from employee emp
left join bonus bon
on emp.empid = bon.empid
where bon.bonus < 1000
or bon.bonus is null;