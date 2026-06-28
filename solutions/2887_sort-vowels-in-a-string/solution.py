class Solution:
    def sortVowels(self, s: str) -> str:
        vow = "AEIOUaeiou"
        res = []
        for c in s:
            if c in vow:
                res.append(c)
        res = sorted(res)
        temp = 0
        ans = ""
        for c in s:
            if c in vow:
                ans+=res[temp]
                temp+=1
            else:
                ans+=c
        return ans
