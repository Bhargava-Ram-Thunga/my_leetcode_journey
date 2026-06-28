class Solution(object):
    def sortedSquares(self, nums):
        res = []
        for i in range(len(nums)):
            res.append(nums[i]**2)
        res.sort()
        return res