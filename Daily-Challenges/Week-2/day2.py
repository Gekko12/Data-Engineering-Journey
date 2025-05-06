class Solution: 
    def selectionSort(self, arr: list) -> list:
        N = len(arr)
        for i in range(N - 1):      # N - 1 as last element is already sorted
            min_element_index = i
            for j in range(i + 1, N):
                if arr[j] < arr[min_element_index]:
                    min_element_index =  j
            arr[i], arr[min_element_index] = arr[min_element_index], arr[i]
        return arr
    
    def bubbleSort(self, arr: list) -> list:
        N = len(arr)
        for i in range(N - 1):
            swap = False    
            for j in range(0, N - i - 1):
                # adjacent max value will swap and move upward like bubble
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swap = True
            if not swap:    # if swap not happen, means all elements are sorted
                break
        return arr                     
                

if __name__ =='__main__':
    arr = [38, 31, 20, 14, 30]
    print('Selection Sort:', Solution().selectionSort(arr))

    arr = [4, 1, 3, 9, 7]
    print('Bubble Sort:', Solution().bubbleSort(arr))
