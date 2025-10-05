from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # TRIANGLE INEQUALITY THEOREM: if a > b > c then checking b + c > a is enough
        nums.sort() 
        for i in range(len(nums) - 3, -1, -1):
            if (nums[i] + nums[i + 1]) > nums[i + 2]:
                return (nums[i] + nums[i + 1] + nums[i + 2])
        return 0


if __name__ == '__main__':
    print(Solution().largestPerimeter([1,2,1,10]))