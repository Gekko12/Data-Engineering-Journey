-- Write your PostgreSQL query statement below

-- odd-and-even-transactions
select transaction_date
    , sum(case when amount % 2 <> 0 then amount else 0 end) as odd_sum
    , sum(case when amount % 2 = 0 then amount else 0 end) as even_sum
from transactions as txn
group by transaction_date
order by transaction_date
;
