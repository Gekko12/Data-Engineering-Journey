from typing import List

class Solution:
    def nCombination2(self, n: int) -> int:
        """
        We have to make the pair, so use nC2 formula, and simplify it.
        """
        return (n * (n - 1)) // 2

    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = {e:0 for e in nums}
        for e in nums:
            dic[e] += 1
        print(dic)
        return sum(self.nCombination2(e) for e in dic.values() if e > 1)


if __name__ == '__main__':
    nums = [1,2,3,1,1,3]
    print(Solution().numIdenticalPairs(nums))