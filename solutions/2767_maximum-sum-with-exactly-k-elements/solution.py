class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        m = max(nums)
        n = m+k-1
        score = int((n*(n+1)/2)-(m*(m+1)/2)) + m
        return score