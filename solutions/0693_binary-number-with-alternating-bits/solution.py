class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        res = bin(n)[2:]
        for i in range(len(res)-1):
            if (res[i] == "1" and res[i+1]!="0") or (res[i] == "0" and res[i+1]!="1"):
                return False
        return True
                