from typing import List

class Solution:
    def sortColorsApproachA(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        It will take O(2N) ~ O(N) time complexity.
        """
        n = len(nums)
        # let's place the 0's at right place
        ptr = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
            print(nums)
        print('----', ptr)        
        # let's place the 1's at right place
        for i in range(ptr, n):
            if nums[i] == 1:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
            print(nums)

    def sortColors(self, nums: List[int]) -> None:
        """
        Approach : Dutch National Flag algorithm
        Time: O(N)
        Space: O(1)
        """
        low, mid, high = 0, 0, len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

if __name__ == '__main__':
    print(Solution().sortColorsApproachA([2,0,2,1,1,0]))
    print(Solution().sortColorsApproachA([2,2,2]))