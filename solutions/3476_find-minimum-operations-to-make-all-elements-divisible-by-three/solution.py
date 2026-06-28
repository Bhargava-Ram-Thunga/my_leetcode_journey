class Solution(object):
    def minimumOperations(self, nums):
        res = 0
        for i in range(len(nums)):
            if nums[i]%3!=0:
                res+=1
        return res
        