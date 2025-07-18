from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Using two-pointer approach
        Time complexity: O(N)
        Space complexity: O(1)
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                break
            elif s < target:
                l += 1
            else:
                r -= 1
        return [l + 1, r + 1]


if __name__ == '__main__':
    print(Solution().twoSum([2,7,11,15], 13))
    print(Solution().twoSum([2,3,4], 5))
    print(Solution().twoSum([-1,0,1,3], 0)) 