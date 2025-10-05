from typing import List

class Solution:
    def trapNotWorking(self, height: List[int]) -> int:
        """
        This will not work as we're unaware of what's coming ahead.
        We should have knowledge of front and back element to solve this problem.
        Fail test Case - [4,2,3]
        """
        ans, n = 0, len(height)

        i = 0
        while i < n:
            j = i + 1

            monotonic_stack, reserve = [-1], []
            while j < n:
                reserve = (reserve + height[i] - height[j]) if height[i] > height[j] else reserve
                reserve.append(height[j])
                if not monotonic_stack:
                    monotonic_stack = [height[j]]
                elif monotonic_stack[-1] < height[j]:
                    monotonic_stack.append(height[j])
                else:
                    while monotonic_stack and monotonic_stack[-1] > height[j]:
                        monotonic_stack.pop()
                    monotonic_stack.append(height[j])
                if height[j] >= height[i]:
                    break
                j += 1
            if height[i] <= monotonic_stack[-1]:
                ans += reserve
                i = j
            else:
                i += 1
        return ans

    def trap(self, height: List[int]) -> int:
        """
        We will use increasing monotonic stack property.
        Example: [0,1,0,2,1]
        left  -> [0,1,1,2,2]
        right <- [2,2,2,2,1]
        formula = [min(left(i), right(i)) - curr_ele(i)]
        """
        n = len(height)

        right_arr = [None] * n
        right_max = height[n - 1]
        for i in range(n - 1, -1, -1) :
            right_max = max(right_max, height[i])
            right_arr[i] = right_max         
        # print(right_arr)
        
        ans = 0
        left_max = height[0]
        for i in range(n):
            left_max = max(left_max, height[i])
            ans += (min(left_max, right_arr[i]) - height[i])
        return ans


if __name__ == '__main__':
    print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(Solution().trap([4,2,0,3,2,5]))    
    print(Solution().trap([4,2,3]))   

