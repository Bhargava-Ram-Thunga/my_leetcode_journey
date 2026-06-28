class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        res =""
        for char in s:
            if char in "()":
                res+=char
        while("()" in res):
            res = res.replace("()","")
            count+=1
        return count