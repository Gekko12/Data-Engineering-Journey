# Week 12 Problem Notes & Links

## Day-1
### Python Problems
- [sort-colors](https://leetcode.com/problems/sort-colors/)
    + [Dutch National Flag Algorithm](https://www.geeksforgeeks.org/dsa/sort-an-array-of-0s-1s-and-2s/)
    + The idea is to sort the array of size n using three pointers: lo = 0, mid = 0 and hi = n - 1 such that the array is divided into three parts -
        * `arr[0]` to `arr[lo - 1]`: This part will have all the zeros.
        * `arr[lo]` to `arr[mid - 1]`: This part will have all the ones.
        * `arr[hi + 1]` to `arr[n - 1]`: This part will have all the twos.

## Day-2
### Python Problems
- [best-time-to-buy-and-sell-stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)