class Solution:
    def getLucky(self, s: str, k: int) -> int:
        intStr = ""
        for i in range(len(s)):
            intStr += str(ord(s[i])-96)
        res = 0
        for i in range(k):
            temp = [int(n) for n in intStr]
            res = sum(temp)
            intStr = str(res)
        return res
