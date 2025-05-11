-- Write your PostgreSQL query statement below

-- Managers with at least 5 direct reports
select emp1.name
from employee emp1
join employee emp2
on emp1.id = emp2.managerid
group by emp1.id, emp1.name
having count(emp1.id) >= 5
;

-- Confirmation rate
-- Approach 1: Using COUNT() and CASE
select sig.user_id, round(count(case when con.action = 'confirmed' then 1 end)  / count(sig.user_id) :: numeric, 2)  confirmation_rate 
from signups sig
left join confirmations con
on sig.user_id = con.user_id
group by sig.user_id
;

-- Approach 2: Using AVG(), but ELSE 0 condition is required otherwise NULL will be printed  
select sig.user_id, round(avg(case when con.action = 'confirmed' then 1 else 0 end) :: numeric, 2)  confirmation_rate 
from signups sig
left join confirmations con
on sig.user_id = con.user_id
group by sig.user_id
;
