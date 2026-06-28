class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        z = 0
        o = 0
        r = max(s.count("0"),s.count("1"))+1
        for i in range(1,r):
            if ("1"*i) in s:
                o = i
            if ("0"*i) in s:
                z = i
        return z<o