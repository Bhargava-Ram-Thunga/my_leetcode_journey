import sys
class Solution:
    def minElement(self, nums: List[int]) -> int:
        n = len(nums)
        res = sys.maxsize
        for i in range(n):
            temp = 0
            for j in str(nums[i]):
                temp += int(j)
            res = min(res,temp)
        return res
