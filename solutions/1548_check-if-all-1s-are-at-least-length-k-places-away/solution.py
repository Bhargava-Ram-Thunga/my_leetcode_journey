class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        ind = []
        for i in range(len(nums)):
            if nums[i] ==1:ind.append(i) 
        for i in range(1,len(ind)):
            if ind[i] - ind[i-1] <=k:
                return False
        return True


