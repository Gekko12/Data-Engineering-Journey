from typing import List

class Solution:
    def triangularSum(self, nums: List[int], last_indx: int = 1) -> int:
        n = len(nums)
        if last_indx == n:
            return nums[0]
        for i in range(n - last_indx):
            nums[i] = (nums[i] + nums[i + 1]) % 10
        # nums[n - last_indx] = -1
        # print(nums, last_indx)
        # print('----------')
        return self.triangularSum(nums, last_indx + 1)
            


if __name__ == '__main__':
    print(Solution().triangularSum([1,2,3,4,5]))