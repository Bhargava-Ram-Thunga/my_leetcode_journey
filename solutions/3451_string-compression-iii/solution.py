import re
class Solution:
    def compressedString(self, word: str) -> str:
        pat = r"(.)\1{0,8}"
        matches = re.finditer(pat,word)
        r = [m.group(0) for m in matches]
        res = ""
        for g in r:
            res += str(len(g))+ g[0]
        return res
