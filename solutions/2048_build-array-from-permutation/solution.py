class Solution(object):
    def buildArray(self, nums):
        res = []
        for i in range(len(nums)):
            res.append(nums[nums[i]])
        return res