def recursion(n):
    if not n:
        return
    print(n, ' - Gaurav')
    recursion(n - 1)

def print1toN(i, n):
    if i > n:
        return
    print('print1toN -', i)
    print1toN(i + 1, n)

def printNto1(i, n):
    if i > n:
        return
    print('printNto1 -', n - i)
    printNto1(i + 1, n)

def sumOfN(n):
    if not n:
        return 0
    return n + sumOfN(n - 1)

def factorial(n):
    if not n:
        return 1
    return n * factorial(n - 1)

class Solution:
    def reverseArray(self, arr):
        l, r = 0, len(arr) - 1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        return arr

    def reverseArrayRecursion(self, arr, n):
        if n <= len(arr)//2:
            return arr
        arr[len(arr)-n], arr[n - 1] = arr[n - 1], arr[len(arr)-n]
        return self.reverseArrayRecursion(arr, n - 1)

    def isPalindrome(self, s: str) -> bool:
        t = ''.join([ch for ch in s.lower() if ch.isalnum()])
        t_size = len(t)
        for i in range(t_size // 2):
            if t[i] != t[t_size-i-1]:
                return False
        return True
    
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)
        
if __name__ == '__main__':
    recursion(5)
    print1toN(0, 3)
    printNto1(0, 3)
    print('Sum of N=5 natural numbers:', sumOfN(5))
    print('Factorial of N=5:', factorial(5))
    print('Reverse an array inplace:', Solution().reverseArray([1,2,3,4,5]))
    print('Reverse an array inplace:', Solution().reverseArrayRecursion([1,2,3,4,5], 5))
    print('IsPalindrome string:', Solution().isPalindrome('A man, a plan, a canal: Panama'))
    print('IsPalindrome string:', Solution().isPalindrome('a121a'))
    print('Fibonacci sum:', Solution().fib(3))
    
