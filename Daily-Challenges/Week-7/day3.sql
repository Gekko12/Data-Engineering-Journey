-- Write your PostgreSQL query statement below

-- top-travellers
select name
    , sum(coalesce(distance, 0)) as travelled_distance
from users u
left join rides r
on u.id = r.user_id
group by r.user_id, u.name
order by travelled_distance desc
    , name asc
