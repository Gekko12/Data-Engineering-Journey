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


if __name__ == '__main__':
    arr = [10, 5, 2, 7, 1, -10]
    print(Solution().longestSubarray(arr, 15))