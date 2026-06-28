class Solution:
    def repeatedCharacter(self, s: str) -> str:
        for i in range(len(s)-1):
            if s[:i+1].count(s[i])==2:
                return s[i]
        return s[-1]