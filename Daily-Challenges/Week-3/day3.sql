-- Write your PostgreSQL query statement below

-- Queries Quality And Percentage
select qry.query_name
    , round(avg(rating :: numeric / position), 2) quality
    , round(avg(case when rating < 3 then 1 else 0 end) * 100.0 , 2) poor_query_percentage 
from queries qry
group by qry.query_name
;