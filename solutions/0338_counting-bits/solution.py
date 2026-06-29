class Solution(object):
    def countBits(self, n):
        res = []
        for i in range(0,n+1):
            biNum = bin(i)[2:]
            res.append(biNum.count("1"))
        return res
        