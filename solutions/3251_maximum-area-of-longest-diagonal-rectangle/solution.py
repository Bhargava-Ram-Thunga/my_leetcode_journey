class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        res = dict()
        for (l,w) in dimensions:
            res[(l**2 + w**2)] = l*w if (l**2 + w**2) not in res else max(l*w,res[(l**2 + w**2)])
        return res[max(res.keys())]