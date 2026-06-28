class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxCandy = max(candies)
        res = []
        for candy in candies:
            if candy+extraCandies>=maxCandy:
                res.append(True)
            else:
                res.append(False)
        return res
        