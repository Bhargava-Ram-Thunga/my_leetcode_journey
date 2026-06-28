from itertools import groupby
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = [len(list(g)) for k,g in groupby(s)]
        ans = 0
        for i in range(len(res)-1):
            if(res[i]<=res[i+1]):
                ans+=res[i]
            else:
                ans+=res[i+1]
        return ans