-- Write your PostgreSQL query statement below

-- Students and examinations
select stu.student_id,
    stu.student_name,
    sub.subject_name, 
    count(exa.student_id) attended_exams
from students stu 
cross join subjects sub
left join examinations exa
on stu.student_id = exa.student_id
and sub.subject_name = exa.subject_name
group by stu.student_id, stu.student_name, sub.subject_name
order by stu.student_id, sub.subject_name ;
