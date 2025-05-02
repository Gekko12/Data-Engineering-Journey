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

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev, temp = 0, x
        while temp > 0:
            digit = temp % 10
            rev = (rev * 10) + digit
            temp //= 10
        return rev == x


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverse(-1230))

    print(sol.isPalindrome(120))
    print(sol.isPalindrome(121))
    print(sol.isPalindrome(-121))