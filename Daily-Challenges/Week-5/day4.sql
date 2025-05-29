-- Write your PostgreSQL query statement below

-- Restaurant growth
select distinct max(c2.visited_on) as visited_on
    , sum(c2.amount) as amount
    , round(sum(c2.amount) :: numeric / 7, 2) as average_amount
from customer c1
left join customer c2
on c2.visited_on between c1.visited_on and c1.visited_on + 6
group by c1.customer_id, c1.visited_on
having count(distinct c2.visited_on) > 6
order by visited_on
;