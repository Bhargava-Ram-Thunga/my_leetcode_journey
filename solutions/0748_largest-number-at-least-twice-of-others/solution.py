class Solution(object):
    def dominantIndex(self, nums):
        ind = nums.index(max(nums))
        nums.sort()
        if nums[len(nums)-2]*2<=nums[len(nums)-1]:
            return ind
        return -1
        