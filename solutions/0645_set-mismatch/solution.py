class Solution:
    def findErrorNums(self, nums: List[int]) -> int:
        n = len(nums)
        res = []
        s = sum(set(nums))
        sumN = n*(n+1)//2
        b = sumN-s
        a = sum(nums)-s
        return [a,b]
