import sys
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        n = len(nums)
        nums = sorted(nums)
        res = sys.maxsize
        for i in range(int(n/2)+1):
            avg = (nums[i]+nums[-1-i])/2
            res = min(res,avg)
        return res
