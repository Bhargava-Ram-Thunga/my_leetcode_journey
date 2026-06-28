def getSum(s:str) -> int:
    return (sum(list(map(lambda x : ord(x)-96,s))))
class Solution:
    def scoreBalance(self, s: str) -> bool:
        for i in range(len(s)+1):
            print(s[:i])
            if(getSum(s[:i+1])==getSum(s[i+1:])):
                return True
        return False