-- Write your PostgreSQL query statement below

-- list-the-products-ordered-in-a-period
select max(p.product_name) as product_name
    , sum(o.unit) as unit
from products p
join orders o
on p.product_id = o.product_id
where o.order_date :: varchar like '2020-02-%'
group by p.product_id
having sum(o.unit) >= 100
;

-- find-users-with-valid-e-mails
-- Approach 1
SELECT *
FROM users
WHERE mail SIMILAR TO '[a-zA-Z]+[a-zA-Z0-9\_.-]*@leetcode.com'
;

-- Approach 2
SELECT *
FROM users
WHERE mail ~ '^[a-zA-Z]+[a-zA-Z0-9_\.-]*@leetcode\.com$'
;