class Solution:
    def addDigits(self, num: int) -> int:
        temp = num
        while(len(str(temp))!=1):
            sumN = 0
            for n in str(temp):
                sumN+=int(n)
            temp = sumN
        return temp

            
