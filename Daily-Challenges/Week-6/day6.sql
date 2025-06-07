-- Write your PostgreSQL query statement below

-- sales-analysis-iii
with cte as (
    select product_id
        , max(sale_date) as max_sale_date 
        , min(sale_date) as min_sale_date
    from sales group by product_id
)
select p.product_id
    , p.product_name
from product p
join cte s
on p.product_id = s.product_id
where s.min_sale_date >= '2019-01-01' 
and  s.max_sale_date <= '2019-03-31'
;
