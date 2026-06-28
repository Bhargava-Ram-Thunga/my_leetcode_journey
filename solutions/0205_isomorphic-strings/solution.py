class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        l = {}
        for i in range(len(s)):
            if (s[i] not in l and t[i] in list(l.values())) or (s[i] in l and l[s[i]] != t[i]):
                return False
            l[s[i]] = t[i]
        return True