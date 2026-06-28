class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            st = max(0,i-nums[i])
            res += sum(nums[st:i+1])
        return res
