class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for a in words:
            if a == a[::-1]:
                return a
        return ""