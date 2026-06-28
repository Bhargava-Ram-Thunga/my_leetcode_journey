class Solution:
    def findComplement(self, num: int) -> int:
        temp = bin(num)[2:]
        res =["1" if b == "0" else "0" for b in temp]
        res = "".join(res).lstrip("0")
        if res:
            return int(res,2)
        return 0