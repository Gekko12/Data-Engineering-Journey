# Week 2 Problem Notes & Links

## Day-1
### Python Problems
- [Frequency of the most frequent element](https://leetcode.com/problems/frequency-of-the-most-frequent-element/)
    + Sliding window principle used #TODO
### SQL Problems
- [Replace employee id with the unique identifier](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/description/?envType=study-plan-v2&envId=top-sql-50)
- [Product sales analysis I](https://leetcode.com/problems/product-sales-analysis-i/description/?envType=study-plan-v2&envId=top-sql-50)

## Day-2
### Python Problems
- [Selection Sort](https://www.geeksforgeeks.org/problems/selection-sort/1)
    + Selection Sort is a comparison-based sorting algorithm. It sorts an array by repeatedly selecting the smallest (or largest) element from the unsorted portion and swapping it with the first unsorted element. This process continues until the entire array is sorted.
    + Time Complexity: O(N^2) // worst-case, best-case, avg-case
    + Space Complexity: O(1)
    + Selection sort is unstable. It means that when sorting an array containing duplicate elements, their relative order might not be preserved after sorting. 
- [Bubble Sort](https://www.geeksforgeeks.org/problems/bubble-sort/1)
    + Bubble Sort works by repeatedly swapping the adjacent elements if they are in the wrong order.
    + Time Complexity: O(N^2) // worst-case, avg-case
    + Time Complexity: O(N) // best-case
    + Space Complexity: O(1)
    + Stable sorting algorithm
### SQL Problems
- [Customer who visited but did not make any transactions](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/?envType=study-plan-v2&envId=top-sql-50)
    + Simply using LEFT OUTER JOIN and filter on NULLS

## Day-3
### Python Problems
- [Insertion Sort](https://www.geeksforgeeks.org/problems/insertion-sort/1)
    + Insertion sort is a simple sorting algorithm that works by iteratively inserting each element of an unsorted list into its correct position in a sorted portion of the list.
    +  It is like sorting playing cards in your hands. You split the cards into two groups: the sorted cards and the unsorted cards. Then, you pick a card from the unsorted group and put it in the right place in the sorted group.
    + Time Complexity: O(N^2) // worst-case, avg-case
    + Time Complexity: O(N) // best-case
    + Space Complexity: O(1)
    + Stable sorting algorithm
### SQL Problems
- [Rising Temperature](https://leetcode.com/problems/rising-temperature/description/?envType=study-plan-v2&envId=top-sql-50)
    + Use of window function LAG()
    + Self or cross join also, can be used

## Day-4
### SQL Problems
- [Average time of process per machine](https://leetcode.com/problems/average-time-of-process-per-machine/description/?envType=study-plan-v2&envId=top-sql-50)
    + Using JOIN and aggregate functions, ROUND(AVG()::numeric, 3)

## Day-5
### SQL Problems
- [Employee Bonus](https://leetcode.com/problems/employee-bonus/?envType=study-plan-v2&envId=top-sql-50)

## Day-6
### SQL Problems
- [Students and examinations](https://leetcode.com/problems/students-and-examinations/description/?envType=study-plan-v2&envId=top-sql-50)
    + CROSS JOIN, LEFT OUTER JOIN and COUNT(specific column) is important here.

## Day-7
### Python Problems
- [Merge Sort](https://www.geeksforgeeks.org/problems/merge-sort/1)
    + Merge sort is a popular sorting algorithm known for its efficiency and stability. It follows the divide-and-conquer approach. It works by recursively dividing the input array into two halves, recursively sorting the two halves and finally merging them back together to obtain the sorted array.
    + Time Complexity: O(Nlog<sub>2</sub>(N)) // worst-case, avg-case, best-case
    + Space Complexity: O(N)
    + Stable sorting algorithm
### SQL Problems
- [Managers with at least 5 direct reports](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/?envType=study-plan-v2&envId=top-sql-50)
    + Interesting question and great example of SELF-JOIN.
- [Confirmation rate](https://leetcode.com/problems/confirmation-rate/description/?envType=study-plan-v2&envId=top-sql-50)
    + Use of `COUNT(CASE WHEN col1='A' THEN 1 ELSE 0)::numeric`, AVG() and LEFT JOIN