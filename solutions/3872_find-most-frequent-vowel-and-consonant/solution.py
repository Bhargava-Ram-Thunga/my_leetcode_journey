class Solution:
    def maxFreqSum(self, s: str) -> int:
        v = {'a':0}
        co = {'b':0}
        for c in set(s):
            if c in "aeiou":
                v[c] = s.count(c)
            else:
                co[c]=s.count(c)
        return max(v.values()) + max(co.values())
        


