class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        k = 0
        res = 0
        while income :
            if(k>0):
                if(income>=brackets[k][0]-brackets[k-1][0]):
                    res += (brackets[k][0]-brackets[k-1][0]) * brackets[k][1]/100
                    income -= (brackets[k][0]-brackets[k-1][0])
                else:
                    res += income * brackets[k][1]/100
                    income = 0
                    break
                if(k==len(brackets)-1):
                    k=0
                else :
                    k+=1
            else:
                if(income>=brackets[k][0]):
                    res += brackets[k][0] *brackets[k][1]/100
                    income -= brackets[k][0]
                    k+=1
                else:
                    res += income * brackets[k][1]/100
                    income = 0
                    break
        return res

