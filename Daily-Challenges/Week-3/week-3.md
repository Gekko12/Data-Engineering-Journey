# Week 3 Problem Notes & Links

## Day-1
### Python Problems
- [Recursive Bubble Sort](https://www.geeksforgeeks.org/recursive-bubble-sort/)
    + Simply replace loops with recursion calls and correct base conditions.
### SQL Problems
- [Not boring movies](https://leetcode.com/problems/not-boring-movies/?envType=study-plan-v2&envId=top-sql-50)
- [Average selling price](https://leetcode.com/problems/average-selling-price/?envType=study-plan-v2&envId=top-sql-50)
    + Very nice question to understand WHERE clause and usage of AND clause with JOIN
    + [sql-join-what-is-the-difference-between-where-clause-and-on-with-and-clause](https://stackoverflow.com/questions/354070/sql-join-what-is-the-difference-between-where-clause-and-on-clause)

## Day-2
### SQL Problems
- [Project employees I](https://leetcode.com/problems/project-employees-i/?envType=study-plan-v2&envId=top-sql-50)
- [Percentage of users attended a contest](https://leetcode.com/problems/percentage-of-users-attended-a-contest/description/?envType=study-plan-v2&envId=top-sql-50)

## Day-3
### Python Problems
- Recursive Insertion Sort
### SQL Problems
- [Queries Quality And Percentage](https://leetcode.com/problems/queries-quality-and-percentage/description/?envType=study-plan-v2&envId=top-sql-50)
    + Use of AVG() with CASE WHEN clause
- [Monthly transactions-I](https://leetcode.com/problems/monthly-transactions-i/?envType=study-plan-v2&envId=top-sql-50)
    + Use of SUBSTR(varchar, index, no_of_char_to_extract) and SUM(CASE WHEN state='approved' THEN 1 ELSE 0 END)

## Day-4
### Python Problems
- [Merge Sort](https://www.geeksforgeeks.org/problems/quick-sort/1)
    + QuickSort is a sorting algorithm based on the Divide and Conquer that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array. It works on the principle of divide and conquer, breaking down the problem into smaller sub-problems.
    + There are mainly three steps in the algorithm:
        1. Choose a Pivot: Select an element from the array as the pivot. The choice of pivot can vary (e.g., first element, last element, random element, or median).
        2. Partition the Array: Rearrange the array around the pivot. After partitioning, all elements smaller than the pivot will be on its left, and all elements greater than the pivot will be on its right. The pivot is then in its correct position, and we obtain the index of the pivot.
        3. Recursively Call: Recursively apply the same process to the two partitioned sub-arrays (left and right of the pivot).
    + Time Complexity: O(Nlog<sub>2</sub>(N)) // avg-case, best-case
    + Time Complexity: O(N^2) // worst-case i.e. occurs when the smallest or largest element is always chosen as the pivot e.g., sorted arrays
    + Space Complexity: O(1)
    + Not a stable sorting algorithm
### SQL Problems
- [Immediate Food Delivery-II](https://leetcode.com/problems/immediate-food-delivery-ii/?envType=study-plan-v2&envId=top-sql-50)

## Day-5
### Python Problems
- []()
### SQL Problems
- [Game Play Analysis IV](https://leetcode.com/problems/game-play-analysis-iv/?envType=study-plan-v2&envId=top-sql-50)
    + **NOTE:** When a problem can be solved using LEAD/LAG and RANK window function, then it can also be solved by using MIN aggregate function