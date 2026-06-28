class Solution:
    def convertToTitle(self, col: int) -> str:
        alpha = list("@ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        res = ""
        while (col>26):
            if col%26==0:
                res += "Z"
                col  = (col//26)-1
            else:
                res += alpha[col%26]
                col //=26
        res += alpha[col]
        return res[::-1]