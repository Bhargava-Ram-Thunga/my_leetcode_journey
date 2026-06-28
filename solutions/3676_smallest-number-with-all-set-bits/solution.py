class Solution:
    def smallestNumber(self, n: int) -> int:
        while(set(bin(n)[2:]) != {"1"}):
            n+=1
        return n