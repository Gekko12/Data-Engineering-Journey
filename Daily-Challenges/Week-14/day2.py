from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        ans = []
        for num in nums:
            if num in seen:
                ans.append(num)
            seen.add(num)
        return ans


if __name__ == '__main__':
    print(Solution().getSneakyNumbers([0,3,2,1,3,2]))