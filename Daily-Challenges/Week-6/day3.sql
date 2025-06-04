-- Write your PostgreSQL query statement below

-- group-sold-products-by-the-date
select sell_date
    , count(distinct product) as num_sold
    , string_agg(distinct product, ',' order by product) as products
from activities
group by sell_date
order by sell_date
;