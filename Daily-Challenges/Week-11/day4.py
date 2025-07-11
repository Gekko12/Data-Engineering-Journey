class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''.join([ch for ch in s.lower() if ch.isalnum()])
        print(t)
        t_size = len(t)
        for i in range(t_size // 2):
            if t[i] != t[t_size-i-1]:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isPalindrome('A man, a plan, a canal: Panama'))