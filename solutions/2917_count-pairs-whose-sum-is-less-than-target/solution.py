class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count =0
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if 0<=i and i<j and j<n and nums[i]+nums[j]<target:
                    count+=1
                else:
                    continue
        return count