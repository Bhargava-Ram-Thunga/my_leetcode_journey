class Solution:
    def countEven(self, num: int) -> int:
        res = 0
        for i in range(2,num+1):
            s = sum(list(map(int,list(str(i)))))
            if s%2==0:
                res += 1
        return res