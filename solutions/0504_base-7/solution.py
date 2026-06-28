class Solution:
    def convertToBase7(self, num: int) -> str:
        temp = abs(num)
        res = ""
        while(temp>=7):
            res += str(temp%7)
            temp //= 7 
        res+=str(temp)
        if num>=0:
            return res[::-1]
        return "-"+res[::-1]
