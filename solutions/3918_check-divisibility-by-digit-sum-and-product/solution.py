import math
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        arr = list(map(int,list(str(n))))
        return n % (sum(arr)+math.prod(arr)) ==0