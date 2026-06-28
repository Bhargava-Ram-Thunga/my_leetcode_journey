class Solution:
    def trailingZeroes(self, n: int) -> int:
        i = 0
        res = 0
        while(n >=  5 ** i):
            print(res)
            print(n)
            i+=1
            res += n//(5**i)
        return res