class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        n = bin(n)[2:][::-1]
        # o = 
        # e = 
        # print(o)
        # print(e)
        return [n[::2].count('1'),n[1::2].count('1')]