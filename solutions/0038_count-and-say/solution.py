class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for i in range(n-1):
            s = "".join([str(len(list(g)))+k for k,g in groupby(s)])
        return s

