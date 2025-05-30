from typing import List

class Solution:
    def missingNumberApproachA(self, nums: List[int]) -> int:
        running_total, index_sum = 0, 0
        for i in range(len(nums)):
            running_total += nums[i]
            index_sum += (i + 1)
        return index_sum - running_total
        # return sum(range(1, len(nums) + 1)) - sum(nums)
    
    def missingNumber(self, nums: List[int]) -> int:
        # we're taking difference of running total and index sum
        # below solution to takle overflow situation
        ans = 0
        for i in range(len(nums)):
            ans += ((i + 1) - nums[i])
        return ans

if __name__ == '__main__':
    print('Missing Numer:', Solution().missingNumber([3, 0, 1, 4, 5]))