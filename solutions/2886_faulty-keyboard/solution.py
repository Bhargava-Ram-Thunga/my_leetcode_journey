class Solution(object):
    def finalString(self, s):
        res = ""
        for i in range(len(s)):
            if s[i]=="i":
                res = res.replace(res[:i],res[i::-1])
            else:
                res+=s[i]
        return res