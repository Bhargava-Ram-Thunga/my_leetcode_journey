class Solution:
    def tribonacci(self, n: int) -> int:
        tribo = [0,1,1]
        for i in range(n-2):
            tribo.append(tribo[i]+tribo[i+1]+tribo[i+2])
        return tribo[n]