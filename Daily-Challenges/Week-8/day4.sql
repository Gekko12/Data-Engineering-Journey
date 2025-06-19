-- Write your PostgreSQL query statement below

-- first-letter-capitalization-II

select content_id
    , content_text as original_text
    , initcap(content_text) as converted_text
from user_content
;