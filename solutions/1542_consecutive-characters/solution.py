class Solution:
    def maxPower(self, s: str) -> int:
        temp = 1
        res = []
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                temp += 1
            else:
                res.append(temp)
                temp = 1
        res.append(temp)
        if len(res)==1:
            return res[0]
        return max(res)

