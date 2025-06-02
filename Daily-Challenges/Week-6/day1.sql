-- Write your PostgreSQL query statement below

-- Delete duplicate emails
-- Approach 1
with cte as (
    select id
        , email
        , rank() over(partition by  email order by id) rnk
    from person
)
delete
from person
where id in (
    select id
    from cte
    where rnk <> 1
)
;

-- Approach 2
delete
from person p1
where exists (
    select p2.id
    from person p2
    where p1.email = p2.email
    and p1.id > p2.id
)
;
