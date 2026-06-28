class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        chars = set(word.lower())
        for char in chars:
            if char.upper() in word and char in word:
                count +=  1
        return count