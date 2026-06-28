class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            res.append(1) if num%2 else res.append(0)
        return sorted(res)