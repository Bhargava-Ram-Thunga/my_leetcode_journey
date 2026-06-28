class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = ""
        while n :
            res = str(n%k) +res
            n//=k
        return sum(map(int,list(res)))