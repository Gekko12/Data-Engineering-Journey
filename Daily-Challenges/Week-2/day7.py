class Solution:
    def merge(self, arr: list, low: int, mid: int, high: int):
        temp = list()
        left, right = low, mid + 1
        # mid is used to act as splitter for the arr
        # both arr[low:mid], arr[mid+1:high] is sorted
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        # once any arr exhaust, we fill the rest
        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= high:
            temp.append(arr[right])
            right += 1
        arr[low : high + 1] = temp
        
        
    def mergeSort(self, arr: list, low: int, high: int):
        if low >= high:
            return
        mid = low + ((high - low) // 2)
        # divide: in-half every time the arr, thats why log2N
        self.mergeSort(arr, low, mid)
        self.mergeSort(arr, mid + 1, high)
        # merge (hypothetically) and sort
        self.merge(arr, low, mid, high)
              

if __name__ =='__main__':
    arr = [38, 31, 20, 14, 30]
    print('Array before:', arr)
    Solution().mergeSort(arr, 0, len(arr) - 1)
    print('Merge Sort:', arr)
