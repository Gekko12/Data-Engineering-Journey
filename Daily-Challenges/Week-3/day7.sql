-- Write your PostgreSQL query statement below

-- Product sales analysis III
with cte as (
    select product_id
        , year
        , quantity
        , price
        , rank() over(partition by product_id order by year) rnk
    from sales
)
select product_id
    , year as first_year
    , quantity
    , price
from cte 
where rnk = 1 
;
-- Input:
-- | sale_id | product_id | year | quantity | price |
-- | ------- | ---------- | ---- | -------- | ----- |
-- | 1       | 100        | 2008 | 10       | 5000  |
-- | 2       | 100        | 2009 | 12       | 5000  |
-- | 7       | 200        | 2011 | 15       | 9000  |
-- | 3       | 100        | 2008 | 10       | 5000  |
-- | 4       | 200        | 2008 | 15       | 9000  |

-- Output:
-- | product_id | first_year | quantity | price |
-- | ---------- | ---------- | -------- | ----- |
-- | 100        | 2008       | 10       | 5000  |
-- | 100        | 2008       | 10       | 5000  |
-- | 200        | 2008       | 15       | 9000  |

-- Classes more than 5-students
select class
from courses
group by class
having count(student) >= 5
;

-- Find followers count
select user_id
    , count(follower_id) as followers_count
from followers
group by user_id
order by user_id 
;