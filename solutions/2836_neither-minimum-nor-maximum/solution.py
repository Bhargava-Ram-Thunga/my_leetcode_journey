class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        maxi = max(nums)
        mini = min(nums)
        for i in range(len(nums)):
            if nums[i]>mini and nums[i]<maxi:
                return nums[i]
        return -1

