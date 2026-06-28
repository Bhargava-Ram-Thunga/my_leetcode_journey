class Solution(object):
    def maximumOddBinaryNumber(self, s):
        count1 = s.count("1")
        count2 = s.count("0")
        return ("1"*(count1-1)+"0"*(count2)+"1")
        