from itertools import groupby
class Solution:
    def countLargestGroup(self, n: int) -> int:
        res = []
        for i in range(1,n+1):
            s = sum(map(int,list(str(i))))
            res.append(s)
        res = sorted(res)
        res2 = [len(list(g)) for k,g in groupby(res)]
        return res2.count(max(res2))