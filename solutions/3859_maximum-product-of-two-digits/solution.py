class Solution:
    def maxProduct(self, n: int) -> int:
        s = list(str(n))
        s.sort()
        return int(s[-1])*int(s[-2])