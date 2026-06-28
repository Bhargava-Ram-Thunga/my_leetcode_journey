class Solution:
    def isBalanced(self, num: str) -> bool:
        res = 0
        for i in range(len(num)):
            if i%2==0:
                res+=int(num[i])
            else:
                res-=int(num[i])
        return res==0