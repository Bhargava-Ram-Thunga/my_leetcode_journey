class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ""
        i = 0
        while i < len(s):
            if i+2 < len(s) and s[i+2] == "#":
                char = int(s[i:i+2])
                res += chr(96+char)
                i+=3
            else:
                char = int(s[i])
                res += chr(96+char)
                i+=1
        return res