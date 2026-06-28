class Solution:
    def minimumMoves(self, s: str) -> int:
        count,i = 0,0
        while i<len(s):
            if s[i]=="X":
                i+=3
                count+=1
            else:
                i+=1
        return count