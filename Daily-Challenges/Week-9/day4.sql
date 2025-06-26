-- Write your PostgreSQL query statement below

-- find-product-recommendation-pairs

-- Approach 1
with order_product_id as (
    select a.user_id
        , a.product_id
        , b.category
    from productPurchases a
    join productInfo b
    on a.product_id = b.product_id
    order by product_id
)
, product_pair as (
    select a.user_id
        , concat(a.product_id, ',', b.product_id) as pair_product_id
        , concat(a.category, ',', b.category) as pair_category
    from order_product_id a
    join order_product_id b
    on a.user_id = b.user_id
    and a.product_id < b.product_id
)
, co_purchase as (
    select pair_product_id
        , pair_category
        , count(user_id) as customer_count
    from product_pair
    group by pair_product_id, pair_category
    having count(user_id) >= 3
)
select split_part(pair_product_id, ',', 1) :: integer as product1_id
    , split_part(pair_product_id, ',', 2) :: integer as product2_id 
    , split_part(pair_category, ',', 1) as product1_category
    , split_part(pair_category, ',', 2) as product2_category 
    , customer_count
from co_purchase
order by customer_count desc, product1_id asc, product2_id asc
;

-- Approach 2
select
    p1.product_id as product1_id,
    p2.product_id as product2_id,
    pi1.category as product1_category,
    pi2.category as product2_category,
    count(p1.user_id) as customer_count
from productpurchases p1
inner join productpurchases p2 
    on p1.user_id = p2.user_id and p1.product_id < p2.product_id
left join productinfo pi1 
    on p1.product_id = pi1.product_id
left join productinfo pi2 
    on p2.product_id = pi2.product_id
group by 1, 2, 3, 4
having count(p1.user_id) >= 3
order by customer_count desc, product1_id, product2_id
;