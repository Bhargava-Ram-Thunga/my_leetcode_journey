class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        for i in range(1,len(nums),2):
            nums[i]*=-1
        return sum(nums)