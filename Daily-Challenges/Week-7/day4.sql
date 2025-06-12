-- Write your PostgreSQL query statement below

-- bank-account-summary-ii

-- nested query to improve the performance
-- since we don't have to calculate sum(amount) again in the HAVING clause
select *
from (
    select name
        , sum(amount) as balance
    from users u
    join transactions t
    on u.account = t.account
    group by u.account, name
) tbl
where balance > 10000
;