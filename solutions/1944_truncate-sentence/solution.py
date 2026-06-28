class Solution(object):
    def truncateSentence(self, s, k):
        r = s.split()
        res = ""
        for i in range(k):
            res+=r[i]
            if i!=k-1:
                res+=" "
        return res

        