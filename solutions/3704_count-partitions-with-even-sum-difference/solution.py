class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(n-1):
            if (sum(nums[:i+1]) - sum(nums[i+1:]))%2==0:
                count+=1
        return count