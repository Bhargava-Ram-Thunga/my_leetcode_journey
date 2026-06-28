class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        alpha = []
        for i in range(len(s)):
            if s[i].isalpha():
                alpha.append(s[i])
        alpha = alpha[::-1]
        res = ""
        k = 0
        for i in range(len(s)):
            if s[i].isalpha():
                res+=alpha[k]
                k+=1
            else:
                res+=s[i]
        return res