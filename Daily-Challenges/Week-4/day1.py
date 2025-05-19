from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums) 
        left = right = 0

        while left < N and right < N:
            print(left, right, nums)
            while right < N and nums[left] == nums[right]:
                right += 1
            left += 1
            if left < N and right < N:
                nums[left] = nums[right]
        return left


if __name__ =='__main__':
    print('>', Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    print('>', Solution().removeDuplicates([0,0]))
    print('>', Solution().removeDuplicates([0]))
    print('>', Solution().removeDuplicates([1,2,3]))
    print('>', Solution().removeDuplicates([1,1,2]))
