class Solution:
    def reformat(self, s: str) -> str:
        a = [c for c in s if c.isalpha()]
        n = [c for c in s if c.isdigit()]
        if(abs(len(a)-len(n)) > 1):
            return ""
        res = ""
        if(len(a) >= len(n)):
            while(a or n):
                if(a):
                    res += a.pop()
                if(n) :
                    res += n.pop()
        elif (len(n) > len(a)):
            while(a or n):
                if(n):
                    res += n.pop()
                if(a) :
                    res += a.pop()
        return res