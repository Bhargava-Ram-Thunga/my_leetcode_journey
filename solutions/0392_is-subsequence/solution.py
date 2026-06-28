class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        ind = 0
        for c in t:
            if ind<len(s) and c == s[ind]:
                ind+=1
        return ind == len(s)