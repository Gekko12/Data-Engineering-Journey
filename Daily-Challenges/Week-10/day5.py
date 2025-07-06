from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        snowball = 0
        for i in range(n):
            if nums[i] == val:
                snowball += 1
            elif snowball:
                nums[i], nums[i - snowball] = nums[i - snowball], nums[i]
        return (n - snowball)

if __name__ == '__main__':
    nums, val = [0, 1, 0, 2, 0, 0, 3], 0
    print(nums, Solution().removeElement(nums, val))
