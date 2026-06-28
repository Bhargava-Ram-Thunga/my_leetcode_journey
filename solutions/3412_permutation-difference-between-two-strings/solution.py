class Solution(object):
    def findPermutationDifference(self, s, t):
        res = 0
        for c in s:
            res+=abs(t.find(c)-s.find(c))
        return res
        