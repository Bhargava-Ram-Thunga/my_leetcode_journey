class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if not(len(nums)%(i+1)):
                res+=nums[i]**2
        return res