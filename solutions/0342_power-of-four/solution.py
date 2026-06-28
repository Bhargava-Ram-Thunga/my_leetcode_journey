import math
class Solution(object):
    def isPowerOfFour(self, n):
        if n<=0:
            return False
        res = log(n,4)
        if res.is_integer():
            return True
        else:
            return False
        