class Solution:                    
    def recursiveInsertionSort(self, arr, i, N):
        if i >= N:
            return
        indx = i
        for j in range(i - 1, -1, -1):
            if arr[indx] < arr[j]:
                arr[indx], arr[j] = arr[j], arr[indx]
                indx = j
            else:
                break
        self.recursiveInsertionSort(arr, i + 1, N)
              

if __name__ =='__main__':
    arr = [38, 31, 20, 14, 30]
    print('Array before:', arr)
    Solution().recursiveInsertionSort(arr, 0, 5)
    print('Recursive insertion sort:', arr)

