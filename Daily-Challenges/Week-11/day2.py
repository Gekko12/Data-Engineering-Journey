from typing import List

class Solution:
    def longestSubarray(self, arr, k):  
        prefix_sum = ans = 0
        map = dict()
        for i in range(len(arr)):  
            prefix_sum += arr[i]
            if prefix_sum == k:
                ans = i + 1
            elif (prefix_sum - k) in map:
                ans = max(ans, i - map[(prefix_sum - k)])
            if prefix_sum not in map:
                map[prefix_sum] = i
            print('Prefix Sum:', prefix_sum, 'Map:', map, 'Ans:', ans)
        return ans

    def twoSumApproachA(self, nums: List[int], target: int) -> List[int]:
        """
        Having time and space complexity of O(N).
        """
        map = {ele : i for i, ele in enumerate(nums)}
        print('\nMap:', map)
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in map and i != map[complement]:
                return [i, map[complement]]
        return []

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        In a single pass, also we can do that.
        """
        hashmap = {}
        for i in range(len(nums)):
            print('Map:', hashmap)
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
        return []

if __name__ == '__main__':
    arr = [10, 5, 2, 7, 1, -10]
    print(Solution().longestSubarray(arr, 15))

    nums = [2,4,11,15]
    # nums = [3,3]
    print(Solution().twoSumApproachA(nums, 6))
    print(Solution().twoSum(nums, 6))