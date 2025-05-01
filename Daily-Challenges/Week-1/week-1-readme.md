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