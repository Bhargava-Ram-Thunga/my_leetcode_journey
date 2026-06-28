class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        r = list(range(len(nums)))
        res = 0
        for i in range(len(nums)):
            if i-k not in r and i+k not in r:
                res+=nums[i]
            elif (i-k) in r and i+k not in r and nums[i]>nums[i-k]:
                res+=nums[i]
            elif i+k in r and i-k not in r and nums[i]>nums[i+k]:
                res+=nums[i]
            elif i-k in r and i+k in r and nums[i]>nums[i-k] and nums[i]>nums[i+k]:
                res+=nums[i]
        return res