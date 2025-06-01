-- Write your PostgreSQL query statement below

-- patients-with-a-condition
-- Approach-1
select *
from patients
where conditions like 'DIAB1%'
or conditions like '% DIAB1%'
;

-- Approach-2
select *
from patients
where exists (
    select 1
    from unnest(string_to_array(conditions, ' ')) tbl
    where tbl like 'DIAB1%'
)
;
