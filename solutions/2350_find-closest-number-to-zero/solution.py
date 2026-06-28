class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = min(list(map(lambda x : abs(x-0),nums)))
        return res if res in nums else -res