# Week 1 Problem Notes & Links

## Day-1
### Python Problems
- [Reverse Integer](https://leetcode.com/problems/reverse-integer/description/)
    + Eg. Input of 123 gives 321, and -120 gives -21
    + Using sign value that way, is insightful
        ```
        temp, sign = abs(num), -1 if num < 0 else 1
        :
        return sign * rev
        ```
- [Is Palindrome](https://leetcode.com/problems/palindrome-number/description/)
    + We can also check it by traversing it half-way like 12321 as 12-3-21
### SQL Problems
- [Recyclable and low-fat products](https://leetcode.com/problems/recyclable-and-low-fat-products/?envType=study-plan-v2&envId=top-sql-50)

## Day-2
### Python Problems
- [Find all divisors](https://www.geeksforgeeks.org/problems/number-of-factors1435/1)
    + Eg. Input of 36 gives [1, 2, 3, 4, 6, 9, 12, 18, 36]
    + Optimal way is to iterate till sqrt(N), for above say 1 -> 6
    + Then for each divisor check its mirror one like 
    ```
    1 pair with 36 (as 1x36=36)
    2 pair with 18 (as 2x18=36)
    3 pair with 12 (as 3x12=36)
    :
    6 pair with itself as 6x6=36
    ```
- [GCD of two numbers](https://www.geeksforgeeks.org/problems/gcd-of-two-numbers3459/1)
    + Eg. Input a=12, b=18 gives output as 6 as greatest common divisor.
    + Optimal way is by using Euclidean algorithm i.e for a > b, gcd(a, b) = gcd(b, a % b)
- [Prime number](https://www.geeksforgeeks.org/problems/prime-number2314/1)
    + Iteration is same as divisor concept as, a prime number is a number greater than 1 that has no positive divisors other than 1 and itself. So, iterate from 2 -> sqrt(N) + 1. FYI, 1 is not a prime number, but 2 is.
### SQL Problems
- [Find customer referee](https://leetcode.com/problems/find-customer-referee/?envType=study-plan-v2&envId=top-sql-50)

## Day-3
### Python Problems
- All about recursion.
- [Reverse an Array Inplace](https://www.geeksforgeeks.org/problems/reverse-an-array/0)
    + Using two pointer approach with left += 1 and right -= 1, till left < right and swap the values with left, right indices.
- [Valid palindrome](https://leetcode.com/problems/valid-palindrome/description/)
    + New function unlocked `str.isalnum()`
- [Fibonacci number](https://leetcode.com/problems/fibonacci-number/)
    + F(0) = 0, F(1) = 1, F(2) = 1, F(3) = 2
### SQL Problems
- [Big Countries](https://leetcode.com/problems/big-countries/?envType=study-plan-v2&envId=top-sql-50)
- [Article View](https://leetcode.com/problems/article-views-i/?envType=study-plan-v2&envId=top-sql-50)