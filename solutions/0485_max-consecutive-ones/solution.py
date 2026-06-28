class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        num = "".join(list(map(str,nums)))
        res = 0
        for n in num.split("0"):
            res = max(res,len(n))
        return res