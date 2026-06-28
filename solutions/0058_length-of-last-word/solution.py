class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip().split()
        return len(s[len(s)-1])