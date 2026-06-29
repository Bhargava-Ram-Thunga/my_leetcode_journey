class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 1
        r = sum(nums[:2])
        k = list(zip(nums[2::2],nums[3::2]))
        res = 1
        for g in k:
            if sum(g) ==r:
                res+=1
            else : 
                break
        return res