from typing import List

class Solution:
    def removeDuplicatesApproachA(self, nums: List[int]) -> int:
        N = len(nums) 
        left = right = 0

        while left < N and right < N:
            print(left, right, nums)
            while right < N and nums[left] == nums[right]:
                right += 1
            left += 1
            if left < N and right < N:
                nums[left] = nums[right]
        return left

    def removeDuplicates(self, nums):
        len_ = len(nums)
        if not len_:
            return 0

        # Use the two pointer technique to remove the duplicates in-place.
        # The first element shouldn't be touched; it's already in its correct place.
        write_ptr = 1

        # Go through each element in the Array.
        for read_ptr in range(1, len_):
            # If the current element we're reading is different to the previous element
            if nums[read_ptr] != nums[read_ptr - 1]:
                nums[write_ptr] = nums[read_ptr]
                write_ptr += 1
        print(nums)
        return write_ptr


if __name__ =='__main__':
    print('>', Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    print('>', Solution().removeDuplicates([0,0]))
    print('>', Solution().removeDuplicates([0]))
    print('>', Solution().removeDuplicates([1,2,3]))
    print('>', Solution().removeDuplicates([1,1,2]))
