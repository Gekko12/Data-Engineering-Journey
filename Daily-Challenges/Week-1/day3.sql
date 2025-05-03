-- Write your PostgreSQL query statement below

-- To find big countries
select name, population, area
from world
where area >= 3000000
or population >= 25000000;

-- Article View
select distinct author_id as id
from views
where author_id = viewer_id;