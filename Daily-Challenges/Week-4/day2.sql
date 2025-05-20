-- Write your PostgreSQL query statement below

-- Customers who bought all products
select customer_id
from customer cust
group by customer_id
having count(distinct cust.product_key) = (
    select count(product_key) 
    from product
)
;

-- The number of employees which report to each employee
select e1.employee_id
    , e1.name
    , count(e2.employee_id) as reports_count
    , avg(e2.age) :: int as average_age
from employees e1
join employees e2
on e1.employee_id = e2.reports_to
group by e1.employee_id, e1.name
order by e1.employee_id
;