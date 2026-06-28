class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res = []
        nums = set(nums)
        mn =min(nums)
        mx = max(nums)
        for i in range(mn+1,mx):
            if i not in nums: 
                res.append(i)
        return res