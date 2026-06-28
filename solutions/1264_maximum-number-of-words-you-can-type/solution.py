class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        for char in brokenLetters:
            text = text.replace(char,".")
        text = text.split()
        count = 0
        for word in text :
            if "." not in word:
                count += 1
        return count