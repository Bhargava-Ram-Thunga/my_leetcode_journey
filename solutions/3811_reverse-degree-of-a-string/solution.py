class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum([ ((97+26-ord(s[i]))*(i+1))for i in range(len(s))])