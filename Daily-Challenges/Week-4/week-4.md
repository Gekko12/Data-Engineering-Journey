# Week 4 Problem Notes & Links

## Day-1
### Python Problems
- [Remove duplicates from sorted-array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)
    + Using two-pointer approach, to solve this.
### SQL Problems
- [Biggest single number](https://leetcode.com/problems/biggest-single-number/description/?envType=study-plan-v2&envId=top-sql-50)
    + Problem is easy, but printing `NULL` require aggregation functional knowledge

## Day-2
### Python Problems
- [Rotate Array](https://leetcode.com/problems/rotate-array/description/)
    + First rotate/reverse the array fully, then reverse the first K-half element then reverse after K-half
    ```
        arr = [1,2,3,4,5]   k = 2
        1. [5,4,3,2,1]      # full array reverse
        2. [4,5 | 3,2,1]    # reverse first K-half 
        3. [4,5 | 1,2,3]    # reverse after K-half
    ```
### SQL Problems
- [Customers who bought all products](https://leetcode.com/problems/customers-who-bought-all-products/?envType=study-plan-v2&envId=top-sql-50)
    + Subquery with GROUP BY HAVING clause
- [The number of employees which report to each employee](https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/description/?envType=study-plan-v2&envId=top-sql-50)
    + Using SELF JOIN

## Day-3
### SQL Problems
- [Primary department for each employee](https://leetcode.com/problems/primary-department-for-each-employee/?envType=study-plan-v2&envId=top-sql-50)

## Day-4
### SQL Problems
- [Triangle judgement](https://leetcode.com/problems/triangle-judgement/?envType=study-plan-v2&envId=top-sql-50)
    + Three line segment can form a triangle if every combination of two sides is greater than third side.
- [Consecutive numbers](https://leetcode.com/problems/consecutive-numbers/description/?envType=study-plan-v2&envId=top-sql-50)
    + Nice question, we can solve this by using JOIN, SUBQUERY as well as LEAD/LAG window functions

## Day-5
### SQL Problems
- [Product price at a given date](https://leetcode.com/problems/product-price-at-a-given-date/?envType=study-plan-v2&envId=top-sql-50)
    + Intersting problem with various approach to solve

## Day-6
### SQL Problems
- [Last person to fit in the bus](https://leetcode.com/problems/last-person-to-fit-in-the-bus/?envType=study-plan-v2&envId=top-sql-50)
    + Very good question, learnt how to use cumulative sum using window functions i.e. `SUM(amount) OVER(ORDER BY transaction_id) AS cumulative_amount`

## Day-7
### SQL Problems
- [Employees whose manager left the company](https://leetcode.com/problems/employees-whose-manager-left-the-company/description/?envType=study-plan-v2&envId=top-sql-50)