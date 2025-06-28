-- Write your PostgreSQL query statement below

-- seasonal-sales-analysis
with season_info as (
    select 
        case 
            when sale_date :: varchar ~ '[0-9]{4}-(01|02|12)-[0-9]{2}' then 'Winter' 
            when sale_date :: varchar ~ '[0-9]{4}-(03|04|05)-[0-9]{2}' then 'Spring'
            when sale_date :: varchar ~ '[0-9]{4}-(06|07|08)-[0-9]{2}' then 'Summer'
            when sale_date :: varchar ~ '[0-9]{4}-(09|10|11)-[0-9]{2}' then 'Fall'
        end as season
        , category
        , sum(quantity) as total_quantity
        , sum(quantity * price) as total_revenue
    from sales s
    join products p
    on s.product_id = p.product_id
    group by season, p.category
)
, most_popular as (
    select *
        , row_number() over(partition by season order by total_quantity desc, total_revenue desc) rnk
    from season_info
)
select season
    , category
    , total_quantity
    , total_revenue
from most_popular
where rnk = 1
order by season
;