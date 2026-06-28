class Solution:
    def residuePrefixes(self, s: str) -> int:
        res = 0
        for i in range(1,len(s)+1):
            if(len(set(s[:i])) == i%3):
                res+=1
        return res
