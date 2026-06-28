class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        r = 0
        for i in range(len(nums)):
            if(nums[i]%2==0):
                r+=1
            if(r==2):
                return True
        return False