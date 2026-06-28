class Solution:
    def binaryGap(self, n: int) -> int:
        temp = bin(n)[2:]
        res = 0
        if temp.count("1")>1:
            li = []
            for i in range(len(temp)):
                if temp[i]=="1":
                    li.append(i)
            for i in range(len(li)-1):
                res = max(res,li[i+1]-li[i])
        return res