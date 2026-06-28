class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)):
            if int(num[::-1][i])%2!=0:
                return num[:len(num)-i]
        return ""

