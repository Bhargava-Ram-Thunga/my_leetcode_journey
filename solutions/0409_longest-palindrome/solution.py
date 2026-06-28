from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        f = dict(Counter(s))
        res = 0
        for v in f.values():
            if v % 2:
                res += v-1
            else:
                res += v
        return res+1 if res < len(s) else res