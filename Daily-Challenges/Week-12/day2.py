from typing import List

class Solution:
    def maxProfitApproachA(self, prices: List[int]) -> int:
        """
        prices : [3,2,6,5,0,3]
        min ->   [3,2,2,2,0,0] (keep the minimum value track via iterate from left to right)
        max <-   [6,6,6,5,3,3] (keep the maximum value track via iterate from right to left)
        diff   : [3,4,4,3,3,3] (difference of max - min)
        Time and space complexity will be O(N).
        """
        n = len(prices)
        left, right = 0, n - 1

        min_arr_left, max_arr_right = [], []
        min_left, max_right = float('inf'), float('-inf')

        while left < n:
            min_left = min(min_left, prices[left]) 
            min_arr_left.append(min_left)
            left += 1

            max_right = max(max_right, prices[right])
            max_arr_right.insert(0, max_right)
            right -= 1
        print(min_arr_left)
        print(max_arr_right)

        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, max_arr_right[i] - min_arr_left[i])
        
        return max_profit
            
    def maxProfit(self, prices: List[int]) -> int:
        """
        Optimal approach having time complexity O(N) and space complexity O(1).
        Similar to previous approach, but better in-terms of space usage.
        """
        max_profit = 0
        min_price = float('inf')

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


if __name__ == '__main__':
    print(Solution().maxProfit([7,1,5,3,6,4]))
    print(Solution().maxProfit([3,2,6,5,0,3]))
    print(Solution().maxProfit([1,0,2]))
