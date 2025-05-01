class Solution:
    def reverse(self, num: int) -> int:
        temp, sign = abs(num), -1 if num < 0 else 1
        rev = 0
        while (temp > 0):
            digit = temp % 10
            rev = (rev * 10) + digit
            temp //= 10
            if rev > ((2**31) -1):
                return 0
        return sign * rev

if __name__ == '__main__':
    sol = Solution()
    print(sol.reverse(-1230))