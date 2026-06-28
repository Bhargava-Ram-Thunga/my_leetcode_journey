class Solution:
    def countAsterisks(self, s: str) -> int:
        count=0
        s = s.split("|")
        for i in range(0,len(s),2):
            count+=s[i].count("*")
        return count