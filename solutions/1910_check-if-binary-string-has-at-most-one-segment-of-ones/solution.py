class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        res = [list(g) for k,g in groupby(s)]
        print(res)
        return len(res) <= 2 