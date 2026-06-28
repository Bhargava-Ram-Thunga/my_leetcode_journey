class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        count = 0
        for i in range(len(s)):
            if s[i]=="(":
                count+=1
                if count == 1:
                    k=i
            if s[i]==")":
                count-=1
                if count == 0:
                    res+=s[k+1:i]
        return res