from typing import List

class Solution:
    def rotateFirstApproach(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k = k % N
        nums[:] = nums[N - k : ] + nums[ : N - k]
    
    def reverse(self, arr: List[int], low: int, high: int) -> None:
        """
        Reverse the array in-place within the range of low to high.
        """ 
        while low < high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1
        

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        K = k % N
        print('>>', nums, self.reverse(nums, 0, N - 1))
        print('>>', nums, self.reverse(nums, 0, K - 1))
        print('>>', nums, self.reverse(nums, K, N - 1))


if __name__ == '__main__':
    nums, k = [1,2,3,4,5,6,7], 3
    print('>', nums, Solution().rotateFirstApproach(nums, k))

    nums, k = [1,2,3,4,5,6,7], 3
    print('>', nums, Solution().rotate(nums, k))
