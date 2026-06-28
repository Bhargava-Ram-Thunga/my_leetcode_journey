class Solution:
    def customSortString(self, order: str, s: str) -> str:
        l = {}
        for i,c in enumerate(order):
            l[c]  = i
        return "".join(sorted(list(s),key = lambda x : l.get(x,0)))