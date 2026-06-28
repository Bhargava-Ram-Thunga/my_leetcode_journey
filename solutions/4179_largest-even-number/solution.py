class Solution:
    def largestEven(self, s: str) -> str:
        for i,c in enumerate(s[::-1]):
            if c == "2":
                return s[:len(s)-i]
        return ""