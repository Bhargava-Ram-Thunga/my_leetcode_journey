class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for num in range(left,right+1):
            for i in range(len(str(num))):
                if int(str(num)[i])==0 or num%int(str(num)[i]):
                    break
            else:
                res.append(num)
        return res

