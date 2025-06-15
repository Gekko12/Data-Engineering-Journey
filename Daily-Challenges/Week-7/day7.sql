-- Write your PostgreSQL query statement below

-- rearrange-products-table
-- Approach 1
select *
from (
    select product_id
        , 'store1' as store
        , store1 as price
    from products
    union
    select product_id
        , 'store2' as store
        , store2 as price
    from products
    union
    select product_id
        , 'store3' as store
        , store3 as price
    from products
) tbl
where price is not null
;

-- Approach 2
SELECT 
    product_id, 
    store,
    price
FROM (
  SELECT 
    product_id, 
    UNNEST(ARRAY['store1', 'store2', 'store3']) AS store,
    UNNEST(ARRAY[store1, store2, store3]) AS price
  FROM 
    Products
) AS unpivot
WHERE price IS NOT NULL
;