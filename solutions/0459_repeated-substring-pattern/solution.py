class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        temp = []
        
        l = len(s)
        if l>1:
            if len(set(s)) == 1:
                return True
        for i in range(2,l):
            if l%i==0:
                temp.append(i)
        
        if temp:
            for num in temp:
                if s[:(l//num)]*num == s:
                    return True
        return False