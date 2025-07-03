-- Write your PostgreSQL query statement below

-- find-category-recommendation-pairs
select pi1.category as category1
    , pi2.category as category2
    , count(distinct pp1.user_id) as customer_count 
from productPurchases as pp1
join productPurchases as pp2
on pp1.user_id = pp2.user_id
join productInfo as pi1
on pp1.product_id = pi1.product_id
join productInfo as pi2
on pp2.product_id = pi2.product_id
where pi1.category < pi2.category
and pi1.category <> pi2.category
group by pi1.category, pi2.category
having count(distinct pp1.user_id) >= 3
order by customer_count desc, category1, category2
;