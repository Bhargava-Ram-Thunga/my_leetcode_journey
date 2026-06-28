class Solution(object):
    def divideArray(self, nums):
        for i in range(len(nums)):
            if nums.count(nums[i])%2!=0 :
                return False
        return True
