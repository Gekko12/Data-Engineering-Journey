-- Write your PostgreSQL query statement below

-- the-latest-login-in-2020
select user_id
    , max(time_stamp) as last_stamp
from logins
where substr(time_stamp :: varchar, 1, 4) = '2020'
-- where time_stamp :: varchar like '2020%'
group by user_id
;