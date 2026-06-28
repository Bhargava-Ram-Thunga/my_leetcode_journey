class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s = dict(Counter(t)- Counter(s))
        # print(sum(s.values()))
        return sum(s.values())