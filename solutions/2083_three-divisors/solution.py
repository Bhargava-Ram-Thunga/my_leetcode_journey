class Solution:
    def isThree(self, n: int) -> bool:
        if n == 2:
            return False
        k = 0
        for i in range(2,n):
            if k>1:
                return False
            if n%i==0:
                k += 1
        return k==1