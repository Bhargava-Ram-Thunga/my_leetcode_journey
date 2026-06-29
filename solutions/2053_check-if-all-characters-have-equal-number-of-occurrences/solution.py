class Solution(object):
    def areOccurrencesEqual(self, s):
        count = s.count(s[0])
        for c in s:
            if s.count(c)!=count:
                return False
        return True
        