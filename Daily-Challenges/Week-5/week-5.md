# Week 5 Problem Notes & Links

## Day-1
### SQL Problems
- [Count salary categories](https://leetcode.com/problems/count-salary-categories/description/?envType=study-plan-v2&envId=top-sql-50)

## Day-2
### Python Problems
- [Move zeroes](https://leetcode.com/problems/move-zeroes/)
    + Use of snowball technique, means accumulating all zeroes as we move forward, having time complexity of O(N).
### SQL Problems
- [Exchange seats](https://leetcode.com/problems/exchange-seats/?envType=study-plan-v2&envId=top-sql-50)

## Day-3
### Python Problems
- [Linear Search](https://www.geeksforgeeks.org/problems/search-an-element-in-an-array-1587115621/1)
- [Union of two sorted arrays](https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1)
    + Using merge-sort kind of approach where we move pointer from array A and B, and which ever is smaller adding it, and moving pointer ahead.
    + Time and Space Complexity: O(N + M), where N and M is size of array A and B respectively
### SQL Problems
- [Movie rating](https://leetcode.com/problems/movie-rating/description/?envType=study-plan-v2&envId=top-sql-50)
    + Nice question which covers, most of the sql aspects

## Day-4
### SQL Problems
- [Restaurant growth](https://leetcode.com/problems/restaurant-growth/description/)
    + Moving average question with window of 7 days

## Day-5
### Python Problems
- [Missing number](https://leetcode.com/problems/missing-number/)
    + Using index sum, and running sum
    + NOTE: Be aware of overflow situation
- [Max consecutive ones](https://leetcode.com/problems/max-consecutive-ones/description/)
- [Single Number](https://leetcode.com/problems/single-number/)
    + Use of XOR (^) operator to detect non-duplicate element
### SQL Problems
- [Friend requests-II who has the most friends](https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/?envType=study-plan-v2&envId=top-sql-50)
    + Question which can be solved using UNION ALL and FULL OUTER JOIN
- [Investements in 2016](https://leetcode.com/problems/investments-in-2016/?envType=study-plan-v2&envId=top-sql-50)
- [Department top three salaries](https://leetcode.com/problems/department-top-three-salaries/?envType=study-plan-v2&envId=top-sql-50)
    + Use of DENSE_RANK

## Day-6
### SQL Problems
- [fix-names-in-a-table](https://leetcode.com/problems/fix-names-in-a-table/?envType=study-plan-v2&envId=top-sql-50)
    + Use of SUBSTR(str, startIndex[, NoOfCharToExtract]), UPPER(), LOWER(), CONCAT()

## Day-7
### SQL Problems
- [patients-with-a-condition](https://leetcode.com/problems/patients-with-a-condition/description/)
    + Good question, learn about UNNEST and EXISTS