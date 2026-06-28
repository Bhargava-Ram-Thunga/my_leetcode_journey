class Solution(object):
    def largestAltitude(self, gain):
        gain.insert(0,0)
        res = [0]
        for i in range(1,len(gain)):
            res.append(gain[i]+res[i-1])
        return max(res)
        