class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for ch in "aeiou":
            if ch in s:
                return True
        return False