# Problems for Recap 

### SQL
- Week-3
    + [Average selling price](https://leetcode.com/problems/average-selling-price/description/)
        * Very nice question to understand WHERE clause and usage of AND clause with JOIN
        * [sql-join-what-is-the-difference-between-where-clause-and-on-with-and-clause](https://stackoverflow.com/questions/354070/sql-join-what-is-the-difference-between-where-clause-and-on-clause)
    + [Game Play Analysis IV](https://leetcode.com/problems/game-play-analysis-iv/?envType=study-plan-v2&envId=top-sql-50)
- Weel-4
    + [Biggest single number](https://leetcode.com/problems/biggest-single-number/description/?envType=study-plan-v2&envId=top-sql-50)
    + [Consecutive numbers](https://leetcode.com/problems/consecutive-numbers/description/?envType=study-plan-v2&envId=top-sql-50)
    + [Product price at a given date](https://leetcode.com/problems/product-price-at-a-given-date/?envType=study-plan-v2&envId=top-sql-50)
    + [Last person to fit in the bus](https://leetcode.com/problems/last-person-to-fit-in-the-bus/?envType=study-plan-v2&envId=top-sql-50)
- Week-5
    + [Exchange seats](https://leetcode.com/problems/exchange-seats/?envType=study-plan-v2&envId=top-sql-50)
    + [Restaurant growth](https://leetcode.com/problems/restaurant-growth/description/)
    + [Friend requests ii who has the most friends](https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/?envType=study-plan-v2&envId=top-sql-50)
    + [Investements in 2016](https://leetcode.com/problems/investments-in-2016/?envType=study-plan-v2&envId=top-sql-50)
    + [patients-with-a-condition](https://leetcode.com/problems/patients-with-a-condition/description/)
        * Learn how to use UNNEST and EXISTS
- Week-6
    + [Delete duplicate emails](https://leetcode.com/problems/delete-duplicate-emails/description/)
    + [find-users-with-valid-e-mails](https://leetcode.com/problems/find-users-with-valid-e-mails/)
        * Learn use of tilde operator `~` and `SIMILAR TO` clause for regex
- Week-7
    + [reformat-department-table](https://leetcode.com/problems/reformat-department-table/)
        * Learn about pivoting
    + [capital-gainloss](https://leetcode.com/problems/capital-gainloss/)
        * Using single `SUM()` to subtract is awesome. 
- Week-8
    + [find-students-who-improved](https://leetcode.com/problems/find-students-who-improved/)
        * Use `FIRST_VALUE` and `LAST_VALUE`, window frame functions
    + [find-invalid-ip-addresses](https://leetcode.com/problems/find-invalid-ip-addresses/)
        * Interesting problem, use `UNNEST`, `STRING_TO_ARRAY`, `CARDINALITY`, and also `ORDER BY` with more than one column in descending order.
- Week-9
    + [analyze-subscription-conversion](https://leetcode.com/problems/analyze-subscription-conversion/description/)
        * **NOTE**: COUNT() does not count NULLs, AVG() ignores NULLs, and SUM() also ignores NULLs.
    + [find-product-recommendation-pairs](https://leetcode.com/problems/find-product-recommendation-pairs/description/)
        * Mind-boggling questions
- Week-10
    + [find-covid-recovery-patients](https://leetcode.com/problems/find-covid-recovery-patients/description/)

### Python
- Week-3
    + [Check if array is sorted and rotated](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/)
- Week-4
    + [Rotate Array](https://leetcode.com/problems/rotate-array/description/)
- Week-5
    + [Move zeroes](https://leetcode.com/problems/move-zeroes/)
    + [Single Number](https://leetcode.com/problems/single-number/)
- Week-6
    + [Longest Subarray with Sum K (+ve elements)](https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1)
- Week-10
    + [remove-element](https://leetcode.com/problems/remove-element/description/)
        * Same as [Move zeroes](https://leetcode.com/problems/move-zeroes/)
        * Use of snowball technique, means accumulating all zeroes as we move forward, having time complexity of O(N), in-place solution.
    + [merge-sorted-array](https://leetcode.com/problems/merge-sorted-array/description/)
        * Twist comes when we do this in O(m+n) time complexity with in-place solution.
- Week-11
    + [Longest Subarray with Sum K (both +ve and -ve elements)](https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1)
        * [Reference tutorial](https://www.geeksforgeeks.org/dsa/longest-sub-array-sum-k/)
        * Very good problem, for +ve element check Week-6, day4.py 
    + [majority-element](https://leetcode.com/problems/majority-element/)
        * Boyer-Moore Majority Voting Algorithm
- Week-12
    + [sort-colors](https://leetcode.com/problems/sort-colors/)
        * [Dutch National Flag Algorithm](https://www.geeksforgeeks.org/dsa/sort-an-array-of-0s-1s-and-2s/)
        * The idea is to sort the array of size n using three pointers: lo = 0, mid = 0 and hi = n - 1 such that the array is divided into three parts -
            - `arr[0]` to `arr[lo - 1]`: This part will have all the zeros.
            - `arr[lo]` to `arr[mid - 1]`: This part will have all the ones.
            - `arr[hi + 1]` to `arr[n - 1]`: This part will have all the twos.