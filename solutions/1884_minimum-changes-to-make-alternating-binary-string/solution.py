class Solution:
    def minOperations(self, s: str) -> int:
        s1 = "01"*((len(s)//2)+2)
        s2 = "10"*((len(s)//2)+2)
        c1 = 0
        c2 = 0
        for i in range(len(s)):
            if s1[i]!=s[i]:
                c1+=1
            if s2[i]!=s[i]:
                c2+=1
        return min(c1,c2)
