-- Write your PostgreSQL query statement below

-- find-consistently-improving-employees
with atleast_three_reviews as (
    select review_id
        , employee_id
        , review_date
        , rating
        , row_number() over(partition by employee_id order by review_date desc) rnk
    from performance_reviews
)
, pivotting_data as (
    select employee_id
        , max(case when rnk = 1 then review_date end) as latest_review_date
        , max(case when rnk = 2 then review_date end) as second_latest_review_date
        , max(case when rnk = 3 then review_date end) as third_latest_review_date
        , max(case when rnk = 1 then rating end) as latest_rating
        , max(case when rnk = 2 then rating end) as second_latest_rating
        , max(case when rnk = 3 then rating end) as third_latest_rating
    from atleast_three_reviews
    where rnk <= 3
    group by employee_id
)
select emp.employee_id
    , emp.name
    , (latest_rating - third_latest_rating) as improvement_score
from pivotting_data as pd
join employees as emp
on pd.employee_id = emp.employee_id
where (
    latest_review_date is not null 
    and second_latest_review_date is not null 
    and third_latest_review_date is not null
)
and (
    latest_rating > second_latest_rating
    and second_latest_rating > third_latest_rating
)
order by improvement_score desc, emp.name
;