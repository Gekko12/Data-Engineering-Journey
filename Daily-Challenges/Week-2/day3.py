class Solution:
    def insertionSort(self, arr: list) -> list:
        N = len(arr)
        # as first element is already in sorted partition
        for i in range(1, N):
            j = i
            # now check for correct place for the element in sorted partition
            while ( j > 0 and arr[j-1] > arr[j]):
                arr[j], arr[j- 1] = arr[j - 1], arr[j]
                j -= 1
        return arr
    
                

if __name__ =='__main__':
    arr = [38, 31, 20, 14, 30]
    print('Selection Sort:', Solution().insertionSort(arr))
