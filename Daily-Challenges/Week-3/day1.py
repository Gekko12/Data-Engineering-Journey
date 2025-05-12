class Solution:
    def recursiveBubbleSort(self, arr, i, j, N):
        if i >= N - 1:
            return
        if j >= N - 1:
            return
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
        self.recursiveBubbleSort(arr, i, j + 1, N)
        self.recursiveBubbleSort(arr, i + 1, j, N)
              

if __name__ =='__main__':
    arr = [38, 31, 20, 14, 30]
    print('Array before:', arr)
    Solution().recursiveBubbleSort(arr, 0, 0, 5)
    print('Recursive bubble sort:', arr)
