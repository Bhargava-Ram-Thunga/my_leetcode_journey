class Solution:
    def countOdds(self, low: int, high: int) -> int:
        c = (high - low) //2
        if high%2 or low%2 :
            return c+1
        return c