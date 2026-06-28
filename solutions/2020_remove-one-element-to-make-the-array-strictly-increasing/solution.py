class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            li = nums[:i]+nums[i+1:]
            if li == sorted(set(li)):
                return True
        return False