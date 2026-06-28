class Solution:
    def largestGoodInteger(self, num: str) -> str:
        li = sorted(set(num),reverse = True)
        for n in li:
            if n*3 in num:
                return n*3 
        return ""