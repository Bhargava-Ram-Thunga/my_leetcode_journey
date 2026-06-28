import math
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        temp = n
        p = math.prod(list(map(int,str(temp))))
        while(p%t!=0):
            temp+=1
            p = math.prod(list(map(int,str(temp))))
        return temp
                
