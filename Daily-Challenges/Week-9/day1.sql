-- Write your PostgreSQL query statement below

-- find-products-with-valid-serial-numbers
select *
from products
where description ~ '(^\D*\s+(SN[0-9]{4}-[0-9]{4})\s*\D*$)|(^(SN[0-9]{4}-[0-9]{4})\s*\D*$)'
order by product_id

