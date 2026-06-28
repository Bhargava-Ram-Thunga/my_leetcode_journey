class Solution:
    def checkString(self, s: str) -> bool:
        return "a" not in s.lstrip("a")
        