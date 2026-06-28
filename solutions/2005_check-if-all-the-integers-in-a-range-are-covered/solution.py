class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        res1 = list(range(left,right+1))
        res2 = []
        for li in ranges:
            res2.extend(range(li[0],li[1]+1))
        res2 = sorted(set(res2))
        res1,res2 = str(res1),str(res2)
        return res1[1:-1] in res2