-- Write your PostgreSQL query statement below

-- find-students-who-improved

-- Approach 1
with cte as (
    select *
        , first_value(score) over(partition by student_id, subject order by exam_date) as first_score
        , first_value(score) over(partition by student_id, subject order by exam_date desc) as last_score
        -- distinct_exam_date_count as (student_id, subject, exam_date) is the primary key for this table
        -- , count(exam_date) over(partition by student_id, subject) as distinct_exam_date_count 
        -- this condition is not required for filter (distinct_exam_date_count <> 1) as first_score
        -- and last_score will do that job, as if a student appears one time only 
        -- then first and last score will be same
    from scores
)
select distinct student_id
    , subject
    , first_score
    , last_score as latest_score
from cte
where first_score < last_score
order by student_id, subject
;
