class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s =s.split()
        if(len(pattern) != len(s)):
            return False
        res = {}
        for i,c in enumerate(pattern):
            if(s[i] in res.values()):
                if(c not in res or (c in res and res[c] != s[i])):
                    return False
            else:
                if c in res and s[i] not in res.values():
                    if(res[c]!=s[i]):
                        return False
                else:
                    res[c] = s[i]
        return True