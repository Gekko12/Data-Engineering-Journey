from typing import List

class Solution:
    def checkFirstApproach(self, nums: List[int]) -> bool:
        N = len(nums)
        left = 0
        right = N - 1

        while left <= (N - 2) and nums[left] <= nums[left + 1]:
            left += 1
        while right >= 1 and nums[right] >= nums[right - 1]:
            right -= 1
        # print(left, right)
        if left == (N - 1) or right == 0:
            return True
        elif nums[0] >= nums[N - 1] and (right - left) == 1:
            return True
        return False

    def checkSecondApproach(self, nums: List[int]) -> bool:
        N = len(nums)
        cnt = 0
        for i in range(N):
            # nums[(i + 1) % N] this will work to compare A[0] and A[N-1]
            print('>', nums[i], nums[(i + 1) % N])
            if nums[i] > nums[(i + 1) % N]:
                cnt += 1
        return cnt <= 1

    def check(self, nums: List[int]) -> bool:
        N = len(nums)
        return sum(nums[i] > nums[(i + 1) % N] for i in range(N)) <= 1


if __name__ == '__main__':
    arr = [3,4,5,1,2]
    # arr = [5,10,6]
    obj = Solution()
    print(obj.checkSecondApproach(arr))
    print(obj.check(arr))