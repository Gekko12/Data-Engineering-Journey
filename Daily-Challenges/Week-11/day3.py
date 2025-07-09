from typing import List

class Solution:
    def majorityElementApproachA(self, nums: List[int]) -> int:
        """
        Time and space complexity will be O(N). Can it be done
        in O(N) time and O(1) space complexity ?
        """
        threshold = len(nums) // 2
        hashmap = dict()
        for ele in nums:
            if ele in hashmap:
                hashmap[ele] += 1
            else:
                hashmap[ele] = 1
        # print(hashmap, threshold)
        for k, v in hashmap.items():
            if v > threshold:
                return k
        return 0

    def majorityElement(self, nums: List[int]) -> int:
        pass
        # [x y x y x]
        #  1 1 2 2 3 (x)
        #  0 1 1 2 2 (y)
        #  1 1 1 1 1
        #  3, 2 ,3, 2, 2, 1
        #  1 1 1 1 2 1
        # 0


if __name__ == '__main__':
    print(Solution().majorityElement([[3,2,3]]))