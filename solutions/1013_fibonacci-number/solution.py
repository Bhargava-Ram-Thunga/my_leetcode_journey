class Solution(object):
    def fib(self, n):
        a = 0
        b = 1
        if n == 1:
            return 1
        elif n==0:
            return 0
        for i in range(2,n+1):
            temp = a+b
            a = b
            b= temp
        return b
        