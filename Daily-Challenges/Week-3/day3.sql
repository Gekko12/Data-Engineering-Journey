-- Write your PostgreSQL query statement below

-- Queries Quality And Percentage
select qry.query_name
    , round(avg(rating :: numeric / position), 2) quality
    , round(avg(case when rating < 3 then 1 else 0 end) * 100.0 , 2) poor_query_percentage 
from queries qry
group by qry.query_name
;

-- Monthly transactions-I
select substr(trans_date :: varchar, 1, 7) as month
    , country
    , count(id) as trans_count 
    , sum(case when state = 'approved' then 1 else 0 end) as approved_count
    , sum(amount) as trans_total_amount
    , sum(case when state = 'approved' then amount else 0 end) as approved_total_amount
from transactions
group by month, country
;