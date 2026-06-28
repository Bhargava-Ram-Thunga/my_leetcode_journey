class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        s = s.split(":")
        sl = s[0][0]
        el = s[1][0]
        sI = int(s[0][1])
        eI = int(s[1][1])
        res = []
        for i in range(ord(el)-ord(sl)+1):
            for j in range(sI,eI+1):
                res.append(f"{chr(ord(sl)+i)}{j}")
        return res