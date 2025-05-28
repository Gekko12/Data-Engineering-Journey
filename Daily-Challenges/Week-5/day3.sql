-- Write your PostgreSQL query statement below

-- Movie rating
with cte1 as (
    select mr.user_id
        , ur.name
        , count(mr.movie_id) as movie_count
    from movieRating mr
    join users ur
    on mr.user_id = ur.user_id
    group by mr.user_id, ur.name
    order by movie_count desc, name asc
    limit 1
)
, cte2 as (
    select mr.movie_id
        , mv.title
        , avg(mr.rating) as avg_rating
    from movieRating mr
    join movies mv
    on mr.movie_id = mv.movie_id
    where created_at BETWEEN '2020-02-01' AND '2020-02-29'
    group by mr.movie_id, mv.title
    order by avg_rating desc, title asc
    limit 1
)
select name as results
from cte1
union all
select title
from cte2
;