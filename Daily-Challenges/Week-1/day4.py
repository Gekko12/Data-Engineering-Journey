class Solution:
    def findFrequency(self, arr: list, x: int) -> int:
        di = dict()
        for ele in arr:
            if ele in di:
                di[ele] += 1
            else:
                di[ele] = 1
        return di[x] if x in di.keys() else 0


if __name__ =='__main__':
    print('Find frequency:', Solution().findFrequency([1,2,2,3,5,1,2,6], 2))
    print('Find frequency:', Solution().findFrequency([1,2,2,3,5,1,2,6], 9))
