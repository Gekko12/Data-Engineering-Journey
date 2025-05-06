-- Write your PostgreSQL query statement below

-- Customer who visited but did not make any transactions
select customer_id, count(1) count_no_trans
from visits vt
left join transactions ts
on vt.visit_id = ts.visit_id
where transaction_id is null
group by customer_id