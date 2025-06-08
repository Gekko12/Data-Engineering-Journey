-- Write your PostgreSQL query statement below

-- market-analysis-i
-- Approach 1
select u.user_id as buyer_id
    , max(u.join_date) as join_date
    , sum(case when to_char(o.order_date, 'YYYY') = '2019' then 1 else 0 end) as orders_in_2019 
from users u
left join orders o
on u.user_id = o.buyer_id
group by u.user_id
order by u.user_id
;

-- Approach 2
select u.user_id as buyer_id
    , max(u.join_date) as join_date
    , count(o.order_id) as orders_in_2019 
from users u
left join orders o
on u.user_id = o.buyer_id
and to_char(o.order_date, 'YYYY') = '2019'
group by u.user_id
order by u.user_id
;
