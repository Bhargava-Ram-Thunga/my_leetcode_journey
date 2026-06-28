class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binary = bin(n)[2:]
        res = ""
        for bit in binary:
            if bit=="1":
                res+="0"
            else:
                res+="1"
        return int(res,2)