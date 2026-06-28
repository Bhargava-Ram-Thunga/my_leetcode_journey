class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        while('#' in s or '#' in t):
            if('#' in s):
                sind = s.index('#')
                s.pop(sind)
                if(sind):
                    s.pop(sind-1)
            if('#' in t):
                tind = t.index('#')
                t.pop(tind)
                if(tind):
                    t.pop(tind-1)
        print(s,t)
        return s == t