class Solution(object):
    def sumZero(self, n):
        res = []
        for i in range(-int(n/2),int(n/2)+1):
            if i>0:
                res.append(-i)
                res.append(i)
        if n%2!=0:
            res.append(0)
        return res
        