class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        for char in s:
            if s.count(char)>1:
                res = max(len(s[s.index(char):len(s)-s[::-1].index(char)-2]),res)
        return res
