class Solution:
    def greatestLetter(self, s: str) -> str:
        li = sorted(list(s),reverse = True)
        for letter in li:
            if letter.isupper() and letter.lower() in li:
                return letter
        return ""