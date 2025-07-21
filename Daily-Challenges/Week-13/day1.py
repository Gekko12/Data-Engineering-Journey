from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, word in enumerate(words) if x in word]


if __name__ == '__main__':
    print(Solution().findWordsContaining(["abc","bcd","aaaa","cbc"], 'c'))
    print(Solution().findWordsContaining(["abc","bcd","aaaa","cbc"], 'z'))
