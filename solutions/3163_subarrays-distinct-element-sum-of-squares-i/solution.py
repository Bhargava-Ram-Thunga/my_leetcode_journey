class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                res += len(set(list(nums[i:j])))**2
        return res