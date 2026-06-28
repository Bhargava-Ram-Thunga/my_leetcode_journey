class Solution:
    def clearDigits(self, s: str) -> str:
        res = []
        for c in s:
            if c.isalpha():
                res.append(c)
            else:
                res.pop()
        return "".join(res) 