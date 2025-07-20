from typing import List

class Solution:
    def containsDuplicateApproachA(self, nums: List[int]) -> bool:
        hashmap = dict()
        for ele in nums:
            hashmap[ele] = hashmap.get(ele, 0) + 1
        print(hashmap)
        for k, v in hashmap.items():
            if v > 1:
                print('Duplicate element:', k)
                return True
        return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Why do we care about counts, we don't need frequency of every element.
        As soon as, we get duplicate return True, else False
        """
        seen = set()
        for ele in nums:
            if ele in seen:
                return True
            seen.add(ele)
        return False

if __name__ == '__main__':
    print(Solution().containsDuplicate([1,2,3,1]))