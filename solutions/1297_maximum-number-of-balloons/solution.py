class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        someDict = {}
        for c in "balon":
            if c == "l" or c=="o":
                someDict[c] = (text.count(c))//2
            else:
                someDict[c] = text.count(c)
        return min(someDict.values())