-- Write your PostgreSQL query statement below

-- find-books-with-no-available-copies
with cte as (
    select bor.book_id
        , count(bor.record_id) current_borrowers
    from borrowing_records bor
    where bor.return_date is null
    group by bor.book_id
)
select b.book_id
    , b.title
    , b.author
    , b.genre
    , b.publication_year
    , a.current_borrowers  
from cte a
join library_books b
on a.book_id = b.book_id
where current_borrowers >= total_copies   -- current_borrowers - total_copies = 0
order by current_borrowers desc, b.title
;