class Solution:
    def alternateDigitSum(self, n: int) -> int:
        NumList = list(str(n))
        res = 0
        for i in range(len(NumList)):
            if i%2==0:
                res+=int(NumList[i])
            else:
                res-= int(NumList[i])
        return res
