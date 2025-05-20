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