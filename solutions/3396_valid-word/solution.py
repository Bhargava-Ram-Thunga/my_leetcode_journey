class Solution:
    def isValid(self, word: str) -> bool:
        word = word.lower()
        al = set("bcdfghjklmnpqrstvwxyz")
        s = set("aeiou")
        return bool(len(word)>=3 and word.isalnum() and (set(word) & s) and (set(word) & al))

