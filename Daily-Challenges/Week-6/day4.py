from typing import List

class Solution:
    def longestSubarrayBrute(self, arr: List[int], k: int) -> int: 
        """
            This is naive approach, having time complexity of O(N^2).
            It works for both negative and positive array elements.
        """
        ans, N = 0, len(arr)
        for i in range(N):
            sum = 0
            for j in range(i, N):
                sum += arr[j]
                if sum == k:
                    ans = max(ans, j - i + 1)
                    print(arr[i:j+1])
                # elif sum > k:
                #     break
        return ans
    
    def longestSubarrayPositive(self, arr: List[int], k: int) -> int: 
        """
            Two-pointer approach, time complexity O(2xN) i.e O(N).
            It will only work for arr[i] >= 0
        """
        N = len(arr)
        left = right = 0
        sum, ans = 0, 0
        while right < N:
            sum += arr[right]
            while left <= right and sum >= k:
                if sum == k:
                    ans = max(ans, right - left + 1)
                sum -= arr[left]
                left += 1
            # print('>', left, right, sum)
            right += 1
        return ans
                

if __name__ == '__main__':
    nums, tgt = [2,3,2,1,1,1,5,11], 5
    nums, tgt = [1,-1,1], 1
    # nums, tgt = [10,5,2,7,1,-10],15
    print(
        'Brute Force: (Positive & Negative) Longest Subarray Length with K Sum:'
        , Solution().longestSubarrayBrute(nums, tgt)
    )
    print(
        'Positive Longest Subarray Length with K Sum:'
        , Solution().longestSubarrayPositive(nums, tgt)
    )