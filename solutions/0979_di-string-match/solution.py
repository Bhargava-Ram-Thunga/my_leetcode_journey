class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = []
        a = 0
        b = len(s)
        for i in range(len(s)):
            if s[i] == "D":
                res.append(b)
                b-=1
            else:
                res.append(a)
                a+=1
        res.append(a)
        return res