# Week 9 Problem Notes & Links

## Day-1
### SQL Problems
- [find-products-with-valid-serial-numbers](https://leetcode.com/problems/find-products-with-valid-serial-numbers/)

## Day-2
### SQL Problems
- [dna-pattern-recognition](https://leetcode.com/problems/dna-pattern-recognition/)

## Day-3
### SQL Problems
- [analyze-subscription-conversion](https://leetcode.com/problems/analyze-subscription-conversion/description/)
    + **NOTE**: COUNT() does not count NULLs, AVG() ignores NULLs, and SUM() also ignores NULLs.
    + It excludes the null values and calculates the average `avg(case when activity_type = 'free_trial' then activity_duration else null end)`