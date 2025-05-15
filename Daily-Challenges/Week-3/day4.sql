-- Write your PostgreSQL query statement below

-- Immediate Food Delivery-II

-- Approach I
with cte as (
    select delivery_id
        , customer_id
        , order_date
        , customer_pref_delivery_date
        , rank() over(partition by customer_id order by order_date asc) rnk
        , case 
            when order_date = customer_pref_delivery_date then 1 
            else 0 
        end as immediate_delivery
    from delivery
)
select round(avg(immediate_delivery) * 100, 2) as immediate_percentage 
from cte
where rnk = 1
;

-- Approach II
with cte as (
    select customer_id
        , min(order_date) as first_order_date
        , min(customer_pref_delivery_date) as min_customer_pref_delivery_date
    from delivery
    group by customer_id
)
select round(avg(case when first_order_date = min_customer_pref_delivery_date then 1 else 0 end) * 100.0, 2) as immediate_percentage
from cte
;