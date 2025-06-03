-- Write your PostgreSQL query statement below

-- second-highest-salary
select max(salary) as SecondHighestSalary
from (
    select id
        , salary
        , dense_rank() over(order by salary desc) rnk
    from employee
) tbl
where rnk = 2
;
