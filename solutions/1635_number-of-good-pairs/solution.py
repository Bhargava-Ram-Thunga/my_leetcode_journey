class Solution(object):
    def numIdenticalPairs(self, nums):
        sum = 0
        res = []
        for i in range(len(nums)):
            t = nums.count(nums[i])
            if nums[i] not in res:
                sum+=t*(t-1)/2
                res.append(nums[i])
        return sum
        