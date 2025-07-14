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
        """
        Boyer-Moore Majority Voting Algorithm
        """
        candid = votes = 0
        for ele in nums:
            if not votes:
                candid, votes = ele, 1
            elif ele == candid:
                votes += 1
            else:
                votes -= 1
            print(f'Candidate: {candid} Votes: {votes}')
        return candid


if __name__ == '__main__':
    print(Solution().majorityElement([1,1,3,1,1,2]))