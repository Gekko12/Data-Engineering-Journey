class Solution:
    def quickSort(self, arr: list, low: int, high: int):
        if low >= high:
            return
        pindex = self.partition(arr, low, high)
        print(pindex, arr, low, high)
        self.quickSort(arr, low, pindex - 1)
        self.quickSort(arr, pindex + 1, high)

    
    def partition(self, arr: list, low: int, high: int) -> int:
        pivot = low     # let's take first element as pivot
        i, j = low, high
        # logic for ascending order arrangement
        while i <= j:
            # find element bigger than pivot from left
            print(arr[low: high + 1], pivot, i, j)
            while i <= high and arr[pivot] >= arr[i]:
                i += 1
            # find elemnt smaller than pivot from right
            while j >= 0 and arr[pivot] < arr[j]:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
            print(i, j)
        # here we find out the correct position of pivot element
        arr[pivot], arr[j] = arr[j], arr[pivot]
        return j
                


if __name__ =='__main__':
    arr = [4,9,5,7,2]
    arr = [4,1,3,9,7]
    arr = [95, 13, 47, 52, 41, 68, 42]
    n = len(arr)
    print('Array before:', arr)
    Solution().quickSort(arr, 0, n - 1)
    print('Quick sort:', arr)

