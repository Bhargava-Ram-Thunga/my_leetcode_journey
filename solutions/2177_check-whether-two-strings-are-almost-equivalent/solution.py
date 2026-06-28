class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        s = set(word1+word2)
        for char in s:
            if abs(word1.count(char)-word2.count(char))>3:
                return False
        return True
        