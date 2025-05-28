class Solution:
    def linearSearch(self, arr: list, x: int) -> int:
        for indx in range(len(arr)):
            if arr[indx] == x:
                return indx
        return -1


    def findUnion(self, a: list, b: list) -> list:
        i, j = 0, 0
        len_a, len_b = len(a), len(b)
        union, last_added = list(), float('inf')

        while i < len_a and j < len_b:
            if a[i] < b[j]:
                if last_added != a[i]:
                    last_added = a[i]
                    union.append(a[i])
                i += 1
            else:
                if last_added != b[j]:
                    last_added = b[j]
                    union.append(b[j])
                j += 1
        
        while i < len_a:
            if last_added != a[i]:
                last_added = a[i]
                union.append(a[i])
            i += 1

        while j < len_b:
            if last_added != b[j]:
                last_added = b[j]
                union.append(b[j])
            j += 1

        return union

         

if __name__ == '__main__':
    print('Index:', Solution().linearSearch([1,2,4,1,5,6,5], 5))
    print('Index:', Solution().linearSearch([1,2,4,1,5,6,5], 9))

    a, b = [1, 2, 4], [2, 3, 3]
    print('Sorted Array Union:', Solution().findUnion(a, b))