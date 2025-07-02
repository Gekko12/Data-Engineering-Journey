-- Write your PostgreSQL query statement below

-- find-drivers-with-improved-fuel-efficiency
with fuel_efficiency as (
    select driver_id
        , avg(case when trip_date between '2023-01-01' and '2023-06-30' then distance_km / fuel_consumed end) as first_half_avg
        , avg(case when trip_date between '2023-07-01' and '2023-12-31' then distance_km / fuel_consumed end) as second_half_avg
    from trips
    group by driver_id
)
select dr.driver_id
    , dr.driver_name
    , round(fe.first_half_avg, 2) as first_half_avg
    , round(fe.second_half_avg, 2) as second_half_avg
    , round(fe.second_half_avg - fe.first_half_avg, 2) as efficiency_improvement 
from fuel_efficiency as fe
inner join drivers as dr
on fe.driver_id = dr.driver_id
where first_half_avg is not null
and second_half_avg is not null
and fe.first_half_avg < fe.second_half_avg
order by efficiency_improvement desc, dr.driver_name
;