class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)
        for i in range(min(l1,l2),0,-1):
            if str1[:i]*(l1//i) == str1 and str1[:i]*(l2//i) == str2:
                return str1[:i]
        return ""
        