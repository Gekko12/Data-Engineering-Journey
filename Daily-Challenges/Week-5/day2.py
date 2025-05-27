from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # using snowball technique, means accumulating all zeroes
        # as moving forward ...0..00..000
        snowball_size = 0
        for i in range(len(nums)):
            if not nums[i]:
                snowball_size += 1
            elif snowball_size > 0:
                nums[i - snowball_size], nums[i] = nums[i], 0

    def moveZeroesA(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # same technique but different code
        i, N = 0, len(nums)
        while i < N:
            if not nums[i]:
                j = i + 1
                while j < N and not nums[j]:
                    j += 1
                if j >= N:
                    break
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
                
      
if __name__ == '__main__':
    nums = [0,3,9,0,12,0,7,0]
    print(nums, Solution().moveZeroes(nums))