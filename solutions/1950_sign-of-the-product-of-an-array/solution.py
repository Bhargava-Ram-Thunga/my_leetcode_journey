class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        fnums = list(filter(lambda x : x < 0,nums))
        k = len(fnums)
        if k%2==0:
            return 1
        return -1
