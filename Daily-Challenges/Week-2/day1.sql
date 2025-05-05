-- Write your PostgreSQL query statement below

-- Replace employee id with the unique identifier
select unique_id, e1.name
from employees e1
left outer join employeeuni e2
on e1.id = e2.id

-- Product sales analysis I
select product_name, year, price
from sales sl
join product pt
on sl.product_id = pt.product_id