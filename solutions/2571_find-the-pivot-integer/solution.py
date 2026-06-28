class Solution(object):
    def pivotInteger(self, n):
        if n==1:
            return 1
        for i in range(1,n-1):
            if i*(i+1)/2==(n*(n+1)/2)-(i*(i-1)/2):
                return i
        return -1
        