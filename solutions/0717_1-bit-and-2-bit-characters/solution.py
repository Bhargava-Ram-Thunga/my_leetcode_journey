class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        bits = "".join(map(str,bits[:-1]))
        while('11' in bits):
            bits = bits.replace('11',"")
        while('10' in bits):
            bits = bits.replace('10',"")
        return set(bits) == {'0'} or bits == ''