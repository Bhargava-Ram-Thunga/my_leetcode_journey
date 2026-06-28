class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []
        for i in range(2**n):
            temp = "0"*(n-len(bin(i)[2:]))+bin(i)[2:]
            if "00" not in temp:
                res.append(temp)
        return res

