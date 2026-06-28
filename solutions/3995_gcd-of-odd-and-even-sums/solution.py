from math import gcd
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        o_sum = 0
        e_sum = 0
        for i in range(2*n):
            if i%2:
                o_sum+= i
            else:
                e_sum+=i
        return gcd(o_sum,e_sum)