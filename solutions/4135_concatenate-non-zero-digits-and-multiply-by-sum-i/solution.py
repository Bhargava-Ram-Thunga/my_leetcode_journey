class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        res = ''
        s = 0
        while n:
            if(n%10!=0):
                res += str(n%10)
                s += n%10
            n//=10
        # print(res,s)
        return int(res[::-1]) * s