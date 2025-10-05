-- Write your PostgreSQL query statement below
with book_id_rating_four_or_more as (
    select book_id
    from reading_sessions
    where session_rating >= 4
)
, book_id_rating_two_or_less as (
    select book_id
    from reading_sessions
    where session_rating <= 2    
)
, book_id_with_five_sessions as (
    select book_id
    from reading_sessions
    group by book_id
    having count(session_id) >= 5
)
, filter_book_id_view as (
    select *
    from book_id_with_five_sessions a
    where exists (
        select 1
        from book_id_rating_four_or_more b
        where a.book_id = b.book_id
    )
    and exists (
        select 1
        from book_id_rating_two_or_less b
        where a.book_id = b.book_id
    )
)
, filter_polarization_score_view as (
    select book_id
        , (max(session_rating) - min(session_rating)) as rating_spread
        , round(sum(case when session_rating <= 2 or session_rating >= 4 then 1 else 0 end) :: numeric / count(session_id), 2) as polarization_score
    from reading_sessions as rsa
    where exists (
        select 1
        from filter_book_id_view as fbv
        where fbv.book_id = rsa.book_id
    )
    group by rsa.book_id
)
select bk.*
    , fpv.rating_spread
    , fpv.polarization_score
from filter_polarization_score_view as fpv
join books as bk
on fpv.book_id = bk.book_id
where fpv.polarization_score >= 0.6
order by fpv.polarization_score desc
    , bk.title desc