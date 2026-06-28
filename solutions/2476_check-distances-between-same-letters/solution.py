class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        for i in range(26):
            alpha = chr(97+i)
            if alpha in s and len(s[s.index(alpha)+1:len(s)-s[::-1].index(alpha)-1])!=distance[i]:
                return False
        return True