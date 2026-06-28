class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return 0
        for i in range(len(nums)):
            if i==0 and nums[i]>nums[i+1]:
                return 0
            elif i== len(nums)-1 and nums[i]>nums[i-1]:
                return len(nums)-1
            else:
                if nums[i] > nums[i-1] and nums[i]>nums[i+1]:
                    return i
