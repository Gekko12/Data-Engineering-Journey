from typing import List

class Solution:
    def mergeApproachA(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        This approach is taking time complexity as O(m+n), but space complexity will be O(n)
        as array will grow when we insert. Also, not a in-place solution
        """
        i, j, k = 0, 0, 0
        res = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                i += 1
                k += 1
            else:
                nums1.insert(k, nums2[j])
                j += 1
                k += 1
        while i < m:
            i += 1
            k += 1
        while j < n:
            nums1.insert(k, nums2[j])
            j += 1
            k += 1
        nums1[:] = nums1[:-n]
        print(nums1)

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        print(nums1)


if __name__ == '__main__':
    nums1, nums2 = [1,2,3,0,0,0], [2,5,6]
    m, n = 3, 3
    # Solution().mergeApproachA(nums1, m, nums2, n)
    Solution().merge(nums1, m, nums2, n)


        