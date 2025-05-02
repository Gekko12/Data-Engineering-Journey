-- Write your PostgreSQL query statement below

-- Find the names of the customer that are not referred by the customer with id = 2
select name
from customer
where referee_id <> 2
or referee_id is null