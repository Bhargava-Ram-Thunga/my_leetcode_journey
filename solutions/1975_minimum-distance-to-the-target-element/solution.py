class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = []
        for i,n in enumerate(nums):
            if n == target:
                res.append(abs(i-start))
        return min(res)