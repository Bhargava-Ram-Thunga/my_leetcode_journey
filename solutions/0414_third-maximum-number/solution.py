class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        x = set(nums)
        if len(x) <3:
            return max(x)
        return sorted(x)[-3]