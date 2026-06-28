class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1 = "0"*(4-len(str(num1)))+str(num1)
        num2 = "0"*(4-len(str(num2)))+str(num2)
        num3 = "0"*(4-len(str(num3)))+str(num3)
        res = ""
        for i in range(4):
            li = [num1[i],num2[i],num3[i]]
            li = list(map(int,li))
            res += str(min(li))
        return int(res)