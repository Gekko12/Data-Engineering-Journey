from typing import List

class Solution:
    def shuffleApproachA(self, nums: List[int], n: int) -> List[int]:
        nums_len = len(nums)
        ans = [None] * nums_len

        for i in range(nums_len):
            if i < n:
                ans[2 * i] = nums[i]
            else:
                ans[2 * (i - n) + 1] = nums[i]
        return ans
    
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
        In-place solution, using the fact that 1 <= nums[i] <= 1000
        """
        nums_len = len(nums)

        # to store the pair of numbers in right half of the original array
        for i in range(n, nums_len):
            nums[i] = (nums[i] * 1024) + nums[i - n]
        
        # to retrive values from the pair of numbers 
        # and placing those retrieved value at their desired position
        index = 0
        for i in range(n, nums_len):
            nums[index] = nums[i] % 1024
            nums[index + 1] = nums[i] // 1024
            index += 2
        return nums

if __name__ == '__main__':
    print(Solution().shuffle([2,5,1,3,4,7], 3))
    print(Solution().shuffle([1,1,2,2], 2))
        