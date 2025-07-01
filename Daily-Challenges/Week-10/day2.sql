-- Write your PostgreSQL query statement below

-- find-covid-recovery-patients

-- Approach 1
with order_data_by_date as (
    select *
    from covid_tests
    order by patient_id, test_date
)
, get_recovery_time as (
    select ct1.patient_id
        , (ct2.test_date - ct1.test_date) as recovery_time
        , row_number() over(partition by ct1.patient_id order by ct1.test_date) rnk
    from order_data_by_date as ct1
    join order_data_by_date as ct2
    on ct1.patient_id = ct2.patient_id
    where ct1.result = 'Positive'
    and ct2.result = 'Negative'
    and ct1.test_date < ct2.test_date
)
select pt.patient_id
    , pt.patient_name
    , pt.age
    , grt.recovery_time
from get_recovery_time as grt
join patients as pt
on grt.patient_id = pt.patient_id
where rnk = 1
order by grt.recovery_time, pt.patient_name
;

-- Approach 2
select pt.patient_id
    , pt.patient_name
    , pt.age
    , (min(ct2.test_date) - min(ct1.test_date)) as recovery_time
from covid_tests as ct1
inner join covid_tests as ct2
on ct1.patient_id = ct2.patient_id
and ct1.result = 'Positive'
and ct2.result = 'Negative'
and ct1.test_date < ct2.test_date
inner join patients as pt
on ct1.patient_id = pt.patient_id
group by pt.patient_id, pt.patient_name, pt.age
order by recovery_time, pt.patient_name
;
