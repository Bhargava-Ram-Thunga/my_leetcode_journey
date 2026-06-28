class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        ind= 0
        for i in range(0,len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                ind+=1
            else:
                break
        s = sum(nums[0:ind+1])
        while (s in nums):
            s+=1
        return s
