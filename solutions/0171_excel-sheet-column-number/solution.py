class Solution:
    def titleToNumber(self, col: str) -> int:
        col = col[::-1]
        res = 0
        for i in range(len(col)):
            res += (26**i)*(ord(col[i])-64)
        return res