-- Write your PostgreSQL query statement below

-- Exchange seats
-- Approach 1
with cte as (
    select max(id) as max_id
    from seat
)
select 
    case 
        when id % 2 = 1 and id + 1 <= cte.max_id then id + 1
        when mod(id, 2) = 0 then id - 1
        else id
    end as id,
    student
from seat, cte
order by id
;

-- Approach 2
with cte as (
    select *
    , case 
        when mod(id, 2) = 0 then id - 1
        else id + 1
      end as id_
    from seat s1
)
select a.id
    , coalesce(b.student, a.student) student 
from seat a
left join cte b
on a.id = b.id_
order by a.id
;
