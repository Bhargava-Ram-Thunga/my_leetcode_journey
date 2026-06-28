class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        res = []
        for i in range(1,n+1):
            if not(n%i):
                res.append(i)
        if len(res) >= k:
            return res[k-1]
        return -1