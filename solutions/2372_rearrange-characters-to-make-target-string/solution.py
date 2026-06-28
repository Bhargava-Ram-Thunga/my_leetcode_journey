class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        tf = dict(Counter(target))
        res = []
        for c in tf:
            res.append(s.count(c)//tf[c])
        # print(res)
        return min(res)