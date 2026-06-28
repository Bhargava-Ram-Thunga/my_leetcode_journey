class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = 1
        temp = 1 
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                temp += 1
            else:
                count = max(temp,count)
                temp =1
        return max(temp,count)