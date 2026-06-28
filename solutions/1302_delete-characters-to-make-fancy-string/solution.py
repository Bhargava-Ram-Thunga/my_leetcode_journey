class Solution:
    def makeFancyString(self, s: str) -> str:
        charSet = set(s)
        for char in charSet:
            while(char*3 in s):
                s = s.replace(char*3,char*2)
        return s