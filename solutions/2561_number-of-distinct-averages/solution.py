class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        res = []
        k = -1
        nums = sorted(nums)
        for i in range(floor(len(nums)/2)):
            res.append((nums[i]+nums[k])/2)
            k-=1
        return len(set(res))

