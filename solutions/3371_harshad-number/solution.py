class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        sumn = 0
        for i in range(len(str(x))):
            sumn+=int(str(x)[i])
        if x%sumn==0:
            return sumn
        return -1
        