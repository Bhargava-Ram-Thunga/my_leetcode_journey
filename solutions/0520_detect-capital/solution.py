class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.islower() or word.istitle() or word.isupper()