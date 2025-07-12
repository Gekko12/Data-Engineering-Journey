class Solution:
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
    print(Solution().isPalindrome(121))