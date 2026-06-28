class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if(target in nums):
            return [nums.index(target),len(nums)-nums[::-1].index(target)-1] 
        return [-1,-1]