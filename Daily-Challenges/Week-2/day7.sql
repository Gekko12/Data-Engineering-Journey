-- Write your PostgreSQL query statement below

-- Managers with at least 5 direct reports
select emp1.name
from employee emp1
join employee emp2
on emp1.id = emp2.managerid
group by emp1.id, emp1.name
having count(emp1.id) >= 5
;

