-- Write your PostgreSQL query statement below

-- Product price at a given date

-- Approach 1
select distinct a.product_id
    , case
        when min(change_date) > '2019-08-16' then 10
        when min(change_date) = '2019-08-16' then (select pr.new_price from products pr where pr.product_id = a.product_id and pr.change_date = '2019-08-16' order by pr.change_date desc limit 1)
        when min(change_date) < '2019-08-16' then (select pr.new_price from products pr where pr.product_id = a.product_id and pr.change_date <= '2019-08-16' order by pr.change_date desc limit 1)
        else max(new_price)
     end as price
from products a
group by a.product_id
;

-- Approach 2
with cte as (
    select product_id
        , max(change_date) as max_change_date
    from products 
    where change_date <= '2019-08-16'
    group by product_id
)
select distinct a.product_id
    , case when max_change_date is null then 10 else new_price end as price 
from products a
left join cte b
on a.product_id = b.product_id
where change_date = max_change_date
or b.product_id is null
;

-- Approach 3
with interim as (
    select product_id,
    new_price as price,
    row_number() over (partition by product_id order by change_date desc) as row_num
    from products
    where change_date <= '2019-08-16'
)
select product_id,
price
from interim
where row_num = 1
union
select product_id, 10 as price
from products 
where product_id not in (select distinct product_id from interim)