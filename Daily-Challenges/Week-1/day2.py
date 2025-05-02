from math import sqrt

class Solution:
    def printDivisors (self, N: int) -> list:
        count = 0
        output = []
        for i in range(1, int(sqrt(N))+1):
            if N % i == 0:
                output.append(i)
                count += 1
                if N % (N/i) == 0 and i != N/i:
                    output.append(int(N/i))
                    count += 1
        output.sort()
        return output

    def gcd(self, a: int, b: int) -> int:
        # where a > b, gcd(a, b) = gcd(b, a % b)
        # where m > n, gcd(m, n) = gcd(n, m % n)
        if a == b:
            return a
        elif a > b:
            m, n = a, b
        else:
            m, n = b, a
        while n != 0:
            m, n = n, m % n
        return m

    def isPrime(self, n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
if __name__ == '__main__':
    print(Solution().printDivisors(36))
    print(Solution().gcd(12, 18))
    print(Solution().isPrime(2), Solution().isPrime(18), Solution().isPrime(37))
