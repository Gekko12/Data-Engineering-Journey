-- Write your PostgreSQL query statement below

-- Not boring movies
select *
from cinema
where id % 2 <> 0
and description not like '%boring%'
order by rating desc
;

-- Average selling price
select distinct prc.product_id
    , coalesce(round(sum(price * units)::numeric / sum(units), 2), 0) as average_price 
from prices as prc
left join unitsSold as unt
on prc.product_id = unt.product_id
and unt.purchase_date between prc.start_date and prc.end_date
group by prc.product_id
;
