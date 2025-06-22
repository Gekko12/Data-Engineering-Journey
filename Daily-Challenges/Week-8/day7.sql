-- Write your PostgreSQL query statement below

-- find-valid-emails
select *
from users
where email similar to '[a-zA-Z_0-9]+@[a-zA-Z]+(.com)'
order by user_id
;

-- find-invalid-ip-addresses
with cte as (
    select log_id
        , ip
        , ip_part
        , cardinality(string_to_array(ip, '.')) as octet_count
    from logs
    cross join unnest(string_to_array(ip, '.')) as ip_part
)
select ip
    , count(distinct log_id) as invalid_count
from cte
where ip_part :: int > 255
or ip_part like '0%'
or octet_count < 4
or octet_count > 4
group by ip
order by invalid_count desc, ip desc
;