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
