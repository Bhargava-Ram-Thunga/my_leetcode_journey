class Solution(object):
    def hammingWeight(self, n):
        return (bin(int(n))[2:]).count("1")
        