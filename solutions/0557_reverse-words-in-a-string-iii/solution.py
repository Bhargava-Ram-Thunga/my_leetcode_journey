class Solution(object):
    def reverseWords(self, s):
        strA = s.split()
        res = ""
        for i in range(len(strA)):
            res+=(strA[i])[::-1]+" "
        return res.strip()