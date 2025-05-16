class Solution:
    def largest(self, arr: list) -> int:
        ans = arr[0]
        for ele in arr:
            if ele > ans:
                ans = ele
        return ans
    
    def getSecondLargest(self, arr: list) -> int:
        first_max = -1
        second_max = -1
        for ele in arr:
            print(first_max, second_max, ele)
            if ele > first_max:
                second_max = first_max
                first_max = ele
            elif ele > second_max and ele != first_max:     # right condition is for duplicate
                second_max = ele
        return second_max

if __name__ == '__main__':
    arr = [13, 2, 7, 45, 5, 98, 23, 7]
    # arr = [10, 5, 10]
    obj = Solution()
    print(f'Largest element in array = {arr} is', obj.largest(arr))
    print(f'Second largest element in array = {arr} is', obj.getSecondLargest(arr))