class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        for c in s:
            if res:
                if c == res[-1]:
                    res.pop()
                else:
                    res.append(c)
            else:
                res.append(c)
        return ''.join(res)