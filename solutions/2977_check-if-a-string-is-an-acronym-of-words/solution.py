class Solution(object):
    def isAcronym(self, words, s):
        if len(words)!=len(s):
            return False
        else:
            res = ""
            for i in range(len(words)):
                res+=(words[i])[0]
            return res==s        